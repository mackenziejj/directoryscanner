import os 
import sys
import traceback
import glob
from dotenv import load_dotenv
load_dotenv()

API_KEY =os.getenv("GG_API_KEY")

from pygitguardian import GGClient
from pygitguardian.config import MULTI_DOCUMENT_LIMIT

client = GGClient(api_key=API_KEY)

#create a list of dictonaries to scan
to_scan = []
for name in glob.glob("/Users/mjackson/Documents/TestSecrets/**"):
    if ".env" in name or os.path.isdir(name):
        continue
    with open(name) as fn:
        to_scan.append({"document": fn.read(), "filename": os.path.basename(name)})

#process our chunks 
to_process = []
for i in range(0, len(to_scan), MULTI_DOCUMENT_LIMIT):
    chunk = to_scan[i : i + MULTI_DOCUMENT_LIMIT]
    try:
        scan = client.multi_content_scan(chunk)
    except Exception as exc:
        traceback.print_exc(2, file=sys.stderr)
        print(str(exc))
    if not scan.success:
        print("Error Scanning some files. Results may be incomplete.")
        print(scan)
    to_process.extend(scan.scan_results)

#printing our results
for i, scan_result in enumerate(to_process):
    if scan_result.has_policy_breaks:
        print(f"{chunk[i]['filename']}: {scan_result.policy_break_count} break/s found")
        #printing policy break type
        for policy_break in scan_result.policy_breaks:
            print(f"\{policy_break.break_type}:")
            #print the matches
            for match in policy_break.matches:
                print(f"\t\t{match.match_type}:{match.match}")

#print results in JSON
for i, scan_results in enumerate(to_process):
    if scan_result.has_policy_breaks:
        print(scan_result.to_json())

#thats it folks 
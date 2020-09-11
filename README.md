# Python Directory Secret Scanner 
This is a simple python script that detects secrets in local files and directories using the [GitGuardian API](https://api.gitguardian.com) and [python wrapper](https://github.com/GitGuardian/py-gitguardian). It is created to help everyone understand how to use GitGuardian API to be able to create custom secrets detection. 


To use this script get an api token from the [GitGuardian Dashboard](https://dashboard.gitguardian.com) and save it in a .env file 

For more checkout the [Blog post](https://blog.gitguardian.com/scan-secrets/) or [YouTube video](https://youtu.be/PgivktH1MxA) 

>Terminology
>Policy Break: GitGuardian scans more than just secrets, we also scan for high risk file extension (example: keystore) and file names (example: .env), when we detect something that breaks the rules of our policies, we call this a policy break.

>Match: A match is the component that triggered a policy break, for example the match of a detected secret will be the secret string itself. A policy break can >have multiple matches.

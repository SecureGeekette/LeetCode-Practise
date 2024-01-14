Collect logs (of any kind) and write a parser which pulls out specific details (domains, executable names, timestamps etc.)


Basics of regex

**1. Literal Characters:
Literal characters in a regex pattern match the exact characters themselves. For example, the regex cat matches the string "cat" in the input text.

**2. Metacharacters:
Metacharacters are special characters with special meanings in regular expressions. Common metacharacters include:

. (Dot): Matches any single character except a newline.
* (Asterisk): Matches zero or more occurrences of the preceding character or group. For example, a* matches "", "a", "aa", "aaa", and so on.
+ (Plus): Matches one or more occurrences of the preceding character or group. For example, a+ matches "a", "aa", "aaa", but not "".
? (Question Mark): Matches zero or one occurrence of the preceding character or group.
| (Pipe): Acts like a logical OR. For example, a|b matches either "a" or "b".

**3. Character Classes:
Character classes allow you to match any one character from a set of characters. For example, [aeiou] matches any vowel, and [^0-9] matches any non-digit.

**4. Anchors:
Anchors are used to specify the position of the match within the text.

^ (Caret): Matches the start of a line.
$ (Dollar): Matches the end of a line.
**5. Quantifiers:
Quantifiers specify how many occurrences of a character or group you want to match.

{n}: Matches exactly n occurrences of the preceding character or group.
{n,}: Matches n or more occurrences.
{n,m}: Matches between n and m occurrences (inclusive).
**6. Escaping Special Characters:
To match a metacharacter as a literal character, you need to escape it with a backslash (\). For example, to match a literal dot, use \..

**7. Groups and Capturing:
Parentheses ( and ) are used to group patterns and capture matched substrings. For example, (ab)+ matches "ab", "abab", "ababab", and so on.

Examples:
\d+: Matches one or more digits.
\b\w+\b: Matches whole words.
^[A-Z][a-z]*$: Matches strings that start with an uppercase letter followed by zero or more lowercase letters.


Assuming we have Apache web server logs, we have to write a parser which details the IP Address, HTTP method, HTTP protocol, HTTP status code, response size, timestamp etc.

127.0.0.1 - - [01/Nov/2023:10:30:42 +0000] "GET /index.html HTTP/1.1" 200 512


import re

sample_text_apache_log = "192.168.1.105 - - [09/Oct/2023:14:32:10 +0000] \"GET /example-page HTTP/1.1\" 200 1234"


ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
timstamp_pattern = "\d{2}\/[A-z][a-z]{2}\/\d{4}"
http_request = "GET|POST"
http_status_code = r"\s\b\d{3}\b\s" #\s is space in regex


ips = re.findall(ip_pattern, sample_text_apache_log)
print("IPs: ")
print(ips)

timestamps = re.findall(timstamp_pattern, sample_text_apache_log)
print("Timestamps: ")
print(timestamps)

requests = re.findall(http_request, sample_text_apache_log)
print("Requests: ")
print(requests)

status_code = re.findall(http_status_code, sample_text_apache_log)
print("Status Codes: ")
print(status_code)



Let's draft a parser for syslogs (syslog is a standard logging protocol used by network devices, servers and applications to send log messages to a central logging server called a syslog server).

Examples:

Simple syslog message: Oct 24 14:32:15 hostname This is a simple syslog message.
Syslog Message with Facility and Severity Levels: Oct 24 14:45:22 localhost.localdomain cron[1234]: (root) CMD ( /usr/local/bin/backup.sh )
Syslog Message with Timestamp, Hostname, and Program Name: 2023-10-24T16:12:30.001Z firewall.example.com firewall: Packet dropped: Suspicious incoming connection from 203.0.113.42
Syslog Message with Custom Information: Oct 24 17:15:28 appserver application: [INFO] User 'alice' successfully created a new account.

Here we'll follow a different regex approach

#This is not working code, just me trying out stuff (ChatGPT suggestions used)

import re

sample_syslog_1 = "Oct 24 14:45:22 localhost.localdomain cron[1234]: (root) CMD ( /usr/local/bin/backup.sh )"
sample_syslog_2 = "2023-10-24T16:12:30.001Z firewall.example.com firewall: Packet dropped: Suspicious incoming connection from 203.0.113.42"
sample_syslog_3 = "Oct 24 17:15:28 appserver application: [INFO] User 'alice' successfully created a new account."

#In inconsistent log formats like these, we have to assume one log format and do fitting

#Instead of doing individual term matching like below
#ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
##message = r"\b:\w+\b"

#ips = re.findall(ip_pattern, sample_syslog_2)
#print("IPs: ")
#print(ips)

#We'll use a named capturing group like this <name>

syslog_pattern = r'(?P<timestamp>.*?)\s(?P<hostname>.*?)\s(?P<program>.*?)\[(?P<process_id>\d+)\]:(?P<message>.*)'
match = re.match(syslog_pattern, sample_syslog_2)

if match:
    groups = match.groupdict()
    # Extracting individual components from the matched groups
    timestamp = groups['timestamp']
    hostname = groups['hostname']
    program = groups['program']
    process_id = groups['process_id']
    message = groups['message']

    print(f'timestamp: {timestamp}, hostname: {hostname}, process_id: {process_id}, message: {message.strip()}')
else:
    # Return None if the syslog message doesn't match the pattern
    print("None")


Log example: (print timestamp and message)
2022-03-24 15:00:01 INFO: Starting server
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:00:05 WARNING: Request from IP 192.168.0.1 was blocked
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:02 ERROR: Could not connect to database
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 Some other message
2022-03-24 15:01:05 INFO: Server shutting down

Solution:
import re

with open("log.txt", "r") as log:
  for line in log:
    match = re.search(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s)(.*)', line)
    if match:
      print("timestamp: " + match.group(1))
      print("message: " + match.group(2))
      print("\n")





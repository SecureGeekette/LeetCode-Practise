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


1. Assuming we have Apache web server logs, we have to write a parser which details the IP Address, HTTP method, HTTP protocol, HTTP status code, response size, timestamp etc.

127.0.0.1 - - [01/Nov/2023:10:30:42 +0000] "GET /index.html HTTP/1.1" 200 512

# Task 1 
On call to this route application need to read content of given file (see file1.txt.. file4.txt)
and render properly it in HTML page. Any markup should be preserved.
files are in English
file 4 contains some Chinese
## file1
![vetty1](https://github.com/Soul-8789/Vetty-Test/assets/102282026/5084f101-0fe1-4b20-b2c0-485e5e1da050)
## file2
![vetty2](https://github.com/Soul-8789/Vetty-Test/assets/102282026/ae19e134-357a-4dd7-ae73-7c064c23ca34)
# file3
![vetty3](https://github.com/Soul-8789/Vetty-Test/assets/102282026/d1b0f047-00d2-4c35-ad82-445d8cd929f6)
# file4
![vetty4](https://github.com/Soul-8789/Vetty-Test/assets/102282026/f37f7971-5548-48a8-9c83-f1c61ba3cc55)

 # Task #2
 Endpoint should accept target file name as optional variable part of URL and default to
file1.txt.

![bydefault](https://github.com/Soul-8789/Vetty-Test/assets/102282026/8ddf7305-cb67-426f-a193-a70378094c1c)

# Task #3
Endpoint should accept optional URL query parameters to specify start line number and
end line number. If those parameters present – return only part of file between specified line
numbers. If parameters absent – return all lines.
![start](https://github.com/Soul-8789/Vetty-Test/assets/102282026/ce0228d7-bb9a-4526-97d7-e1558a16a6ce)

# Task #4
 All most likely exceptions in application logic should be handled gracefully. When
exception happens error page should be displayed with exception details
![error](https://github.com/Soul-8789/Vetty-Test/assets/102282026/ea753cdd-0bc7-4d3d-a0ef-4eb9b198d5cf)

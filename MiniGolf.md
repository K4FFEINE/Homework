# Mini Golf

## Solution
- Used curl -X followed by url please see screen shots below.  Flag appeared to be encoded using base 64, which was correct once I decoded.


<img width="854" alt="Screen Shot 2020-11-23 at 12 45 48 AM" src="https://user-images.githubusercontent.com/74154888/99932390-dbd2d780-2d25-11eb-8dcc-4b5315a03235.png">








###Command
-Curl will transfer data to or from a server
###Options
- The -X flag specifies a custom request method to use when communicating with the HTTP server. By default, the GET method is used unless some other method is specified.
- Use "PUT" to update instead of GET, which is the default
- echo the encoded flag
- pipe into base64 with -d to decode it

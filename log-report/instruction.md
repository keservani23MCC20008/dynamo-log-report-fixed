An Apache-style access log is in the working directory at `/app/access.log`. Each line begins with the client IP address and contains a quoted HTTP request line such as `"GET /index.html HTTP/1.1"`.

Read that log and write a JSON summary to the absolute path `/app/report.json`. The JSON must be a single object with exactly these three keys:

- `total_requests`: an integer, the number of non-empty request lines in the log.
- `unique_ips`: an integer, the count of distinct client IP addresses (the first whitespace-separated field on each line).
- `top_path`: a string, the request path that appears most often across all requests (for example `/index.html`).

Success criteria:

1. The file `/app/report.json` exists and contains a single valid JSON object.
2. `total_requests` equals the number of non-empty lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IP addresses in the log.
4. `top_path` equals the most frequently requested path in the log.

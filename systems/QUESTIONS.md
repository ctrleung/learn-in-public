# Questions to come back to (systems)

Systems and cloud questions that came up while studying or at work. At the start of a systems session, check whether any question's topic is coming up; when you reach it, answer it, then tick it off. Parked topics (AWS, Linux and so on) are in `PARKING-LOT.md` and are not worked on unless asked. Questions only, nothing personal.

| Done | Question | Where it is covered | When |
|---|---|---|---|
| [ ] | What is a customer-managed key (CMK)? How does it relate to encryption at rest vs in transit, and how do the cloud providers (AWS KMS, Azure Key Vault, Google Cloud KMS) differ? | `PARKING-LOT.md` (AWS and cloud), related to the TLS ideas in `networking/TOPICS.md` | parked: only when asked |
| [ ] | SSE-S3 vs SSE-KMS: how the two server-side encryption options for S3 differ, and when to use each | `PARKING-LOT.md` (AWS; security beyond the browser: cryptography); related to the customer-managed key question above | parked: only when asked |
| [ ] | KMS key policies vs IAM permissions: how they work together, and which one decides access to a key | `PARKING-LOT.md` (AWS, IAM; security beyond the browser: identity) | parked: only when asked |
| [ ] | CloudFront origin access control (OAC): how CloudFront identifies itself to S3, and why it needs `kms:Decrypt` when the bucket uses a KMS key | `PARKING-LOT.md` (AWS); the CDN idea is in `networking/TOPICS.md`, "Hosting, domains and CDNs" | parked: only when asked |
| [ ] | CloudFront cache behaviours: how paths are matched, and how caching, headers and TTLs are set per behaviour | the caching ideas are in `web/TOPICS.md`, "HTTP caching" (web plan week 9, 18 to 24 Jan) and the systems caching and CDN sessions; the CloudFront settings are in `PARKING-LOT.md` (AWS) | the HTTP caching part: week 9; the CloudFront part: parked |
| [ ] | S3 server-side copy: what it is, how it differs from downloading and re-uploading, and what it does to encryption and metadata | `PARKING-LOT.md` (AWS) | parked: only when asked |
| [ ] | Lambda timeouts, SQS retries and dead-letter queues: how they interact, and what happens to a message that keeps failing | `PARKING-LOT.md` (AWS; backend and databases; operations and monitoring) | parked: only when asked |
| [ ] | Deploy roles and `prevent_destroy` in OpenTofu: what each does and how they protect infrastructure | `PARKING-LOT.md` (DevOps: infrastructure as code; AWS, IAM) | parked: only when asked |

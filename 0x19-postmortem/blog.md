
**Incident Overview:**
On 14-02-2024, our shopping website encountered connectivity and functionality issues, leading to customer complaints and internal team difficulties. Investigation revealed problems with photo sizes, resolutions, PHP admin settings, and server configurations.

**Incident Report**

**Timeline**

14-02-2024 9:55 AM GMT+1: A customer reported difficulties connecting to our shopping website and making payments.
14-02-2024 10:20 AM GMT+1: Our internal team experienced similar issues accessing the website.
14-02-2024 10:35 AM GMT+1: Initial investigation began into the website's functionality.
12-02-2024 10:40 AM GMT+1: Suspicions arose regarding possible issues with photo sizes and resolutions.
14-02-2024 10:42 AM GMT+1: Examination of the PHP admin and server configurations commenced.
15-02-2024 10:45 AM GMT+1: Concerns were raised about mismatches in photo dimensions and improper server settings.
15-02-2024 10:00 AM GMT+1: Focus shifted towards potential problems with image handling and server connectivity.
15-02-2024 11:00 AM GMT+1: The incident was escalated to the development team for further investigation.
15-02-2024 11:20 AM GMT+1: Resolution was achieved by adjusting photo sizes and resolutions, and resolving PHP admin and server issues.

**Root Cause And Resolution**
The website faced connectivity and functionality issues due to incorrect photo sizes and resolutions, as well as PHP admin and server configuration problems. These issues prevented customers from accessing the website properly and making payments. Resolution was achieved by rectifying the photo dimensions, ensuring proper server settings, and addressing PHP admin issues.

**Corrective And Preventative Measures**

Implement continuous integration pipelines to conduct build checks on pull request branches before merging with deployment branches.
Establish monitoring systems for database and application servers to promptly identify and address any issues.
Develop and enforce testing protocols for new features, ensuring their successful completion before merging with deployment branches.

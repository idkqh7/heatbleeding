Test 1Password database for Heart Bleeding problems
============

Test script for 1Password database for SSL Heart Bleeding (CVE-2014-0160)

To test 1Password database export it to local disk. Locate file data.1pif and run in same directory:
```
git clone https://github.com/aefimov/heatbleeding.git
./heatbleeding/test_1password_ssl_hosts.sh
```

If all OK, then remove exported database from disk. If some hosts show `WARNING`, then you probably need to change password on such host.

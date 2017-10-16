# ctl-results
Results of Cyber Test Lab analysis

## Caveat hackor

I'm beginning to push some preliminary results for [Fedora 26](https://github.com/fedoraredteam/ctl-results/tree/master/fedora/26). The [CTL](https://github.com/fedoraredteam/cyber-test-lab) code is still very alpha. Translation: this data sucks.

We're still working on this, so check back for updates.

## Sample data

When the tool works right, here's a sample result, taken from [BEDTools-2.26.0-3.fc26.x86_64.rpm](https://github.com/fedoraredteam/ctl-results/blob/master/fedora/26/B/BEDTools-2.26.0-3.fc26.x86_64.rpm.json)

```json
{
    "results": {
        "usr/bin/bedtools": {
            "report-functions": [
                "_ZNSo9_M_insertImEERSoT_", 
                "_ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE5rfindEcm", 
                "select", 
                "_ZNSt8__detail15_List_node_base7_M_hookEPS0_", 
                "_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEaSEOS4_", 
                "__cxa_throw", 
                "_ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7compareERKS4_", 
                "__cxa_guard_abort", 
                "__fxstat", 
                "connect", 
                "fputs", 
                "fileno", 
                "_ZNSt13runtime_errorD1Ev", 
                "__cxa_free_exception", 
                "__memcpy_chk", 
                "_ZNSt12__basic_fileIcED1Ev", 
                "isspace", 
                "ioctl", 
                "fopen", 
                "strftime", 
                "strcat", 
                "truncated..."
            ], 
            "rpm": "BEDTools-2.26.0-3.fc26.x86_64.rpm", 
            "find-libc-functions": [
                "truncated...",
                "longjmp", 
                "mbsnrtowcs", 
                "mbsrtowcs", 
                "mbstowcs", 
                "memcpy", 
                "memmove", 
                "mempcpy", 
                "memset", 
                "obstack_printf", 
                "obstack_vprintf", 
                "poll", 
                "ppoll", 
                "pread64", 
                "pread", 
                "printf", 
                "ptsname_r", 
                "read", 
                "readlink", 
                "readlinkat", 
                "realpath", 
                "recv", 
                "recvfrom", 
                "snprintf", 
                "sprintf", 
                "stpcpy", 
                "stpncpy", 
                "strcat", 
                "strcpy", 
                "strncat", 
                "strncpy", 
                "swprintf", 
                "truncated..."
            ], 
            "hardening-check": {
                " Read-only relocations": "yes", 
                " Position Independent Executable": "no, normal executable!", 
                " Stack protected": "yes", 
                " Fortify Source functions": "yes (some protected functions found)", 
                " Immediate binding": "no, not found!"
            }, 
            "filename": "usr/bin/bedtools"
        }, 
        "complexity": {
            "r2 aa": {
                "afCc": 48, 
                "afC": 804
            }
        }
    }, 
    "metadata": {
        "spec_data": {
            "Group": " Applications/Engineering", 
            "Name": " BEDTools", 
            "License": " GPLv2+", 
            "URL": " https://github.com/arq5x/bedtools", 
            "Relocations": " (not relocatable)", 
            "Install Date": " (not installed)", 
            "Build Host": " buildvm-10.phx2.fedoraproject.org", 
            "Description": "\n\nThe BEDTools utilities allow one to address common genomics tasks such\nas finding feature overlaps and computing coverage. The utilities are\nlargely based on four widely-used file formats: BED, GFF/GTF, VCF, and\nSAM/BAM. Using BEDTools, one can develop sophisticated pipelines that\nanswer complicated research questions by \"streaming\" several BEDTools\ntogether.\n", 
            "Build Date": " Fri 10 Feb 2017 12:03:44 AM EST", 
            "Source RPM": " BEDTools-2.26.0-3.fc26.src.rpm", 
            "Version": " 2.26.0", 
            "Architecture": " x86_64", 
            "Signature": " RSA/SHA256, Mon 13 Feb 2017 03:04:12 PM EST, Key ID 812a6b4b64dab85d", 
            "Release": " 3.fc26", 
            "Vendor": " Fedora Project", 
            "Packager": " Fedora Project", 
            "Summary": " A flexible suite of utilities for comparing genomic features", 
            "Size": " 13497477"
        }
    }
}
```

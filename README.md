# conan-inih
inih library package for conan.io https://github.com/benhoyt/inih

# Bintray repository
Find conan package here: https://bintray.com/radalytica/conan-radalytica/inih:radalytica

# release notes
## 44 
packages this release from @benhoyt https://github.com/benhoyt/inih/tree/r44
## v44.1
packages this fork from @mohamedghita https://github.com/mohamedghita/inih/tree/r44.1. which supports vectors of string, integer, boolean, and real. The release extends the class INIReader by inih::extended::INIReaderVec.
For example:
```ini
real_array = [0.0, 1.1, -1.1]
integer_array = [0, 1, -1]
boolean_array = [false, true]
string_array = [hello, array]
```

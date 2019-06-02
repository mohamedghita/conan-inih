# conan-inih
inih library package for conan.io https://github.com/benhoyt/inih

# Bintray repository
Find conan package here: https://bintray.com/radalytica/conan-radalytica/inih:radalytica

# release notes
## v44.1
support vectors of string, integer, boolean, and real. The release extends the class INIReader by inih::extended::INIReaderVec.
For example:
```ini
real_array = [0.0, 1.1, -1.1]
integer_array = [0, 1, -1]
boolean_array = [false, true]
string_array = [hello, array]
```

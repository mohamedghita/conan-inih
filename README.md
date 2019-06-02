# conan-inih
inih library package for conan.io https://github.com/benhoyt/inih

# Bintray repository
Find conan package here: https://bintray.com/radalytica/conan-radalytica/inih:radalytica

# Installation 
1. [install conan.io](https://docs.conan.io/en/latest/installation.html) 
2. setup bintray repo
3. install inih
* In a nuteshell, run these three commands:
```bash
pip install conan
conan remote add conan-radalytica https://api.bintray.com/conan/radalytica/conan-radalytica
conan install --reomte conan-radalytica inih/44.1@radalytica/stable
```

For more inormation, refer to [conan.io](https://docs.conan.io/en/latest/) and [inih](https://github.com/mohamedghita/inih/tree/r44.1) documentation

# release notes
## v44 
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

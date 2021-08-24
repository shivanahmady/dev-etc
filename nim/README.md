edu-nim 

Nimble Programming Language Learning 
=========================================
- [https://nim-lang.org/docs/tut1.html]

# PROJECTS DIRECTORY
## 1. dmidecode (dmi/smbios parser)
- [x] dmi/smbios table decode reference [https://linux.die.net/man/8/dmidecode]



#### Notes & Essential Commands 

**Compile / Run**
- `nim compile --run greetings.nim`
- `nim c -r greetings.nim`

**Release**
- `nim c -d:release greetings.nim`

**Args**
- `nim compile --run greetings.nim arg1 arg2`

**String Literals**
String literals are enclosed in double quotes; character literals in single quotes. Special characters are escaped with \: \n means newline, \t means tabulator, etc. There are also raw string literals:

> `r"C:\program files\nim"`

In raw literals the backslash is not an escape character.
The third and last way to write string literals are long string literals. They are written with three quotes: """ ... """; they can span over multiple lines and the \ is not an escape character either. They are very useful for embedding HTML code templates for example.
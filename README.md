[contributors-shield]: https://img.shields.io/github/contributors/Alessandro-Salerno/Hackdecomp.svg?style=flat-square
[contributors-url]: https://github.com/Alessandro-Salerno/Hackdecomp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Alessandro-Salerno/Hackdecomp.svg?style=flat-square
[forks-url]: https://github.com/Alessandro-Salerno/Hackdecomp/network/members
[stars-shield]: https://img.shields.io/github/stars/Alessandro-Salerno/Hackdecomp.svg?style=flat-square
[stars-url]: https://github.com/Alessandro-Salerno/Hackdecomp/stargazers
[issues-shield]: https://img.shields.io/github/issues/Alessandro-Salerno/Hackdecomp.svg?style=flat-square
[issues-url]: https://github.com/Alessandro-Salerno/Hackdecomp/issues
[license-shield]: https://img.shields.io/github/license/Alessandro-Salerno/Hackdecomp.svg?style=flat-square
[license-url]: https://github.com/Alessandro-Salerno/Hackdecomp/blob/master/LICENSE.txt

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![](https://tokei.rs/b1/github/Alessandro-Salerno/Hackdecomp)
![shield](https://img.shields.io/static/v1?label=version&message=0.1.0&color=blue) 


# Hackdecomp
Hackdecomp is a disassembler made for VM-O-MATIC to avoid mistakes in the development of other software based on the specification.

## Installing Hackdecomp
* Windows:
```
pip install git+https://github.com/Alessandro-Salerno/Hackdecomp
```
* macOS/Linux:
```
pip3 install git+https://github.com/Alessandro-Salerno/Hackdecomp
```

## Usage
- Windows: `pyhHackdecomp.py <start offset> <end offset or 0>`
- Linux/macOS: `python3 hackdecomp.py <start offset> <end offset or 0>`

## Example
Given the following input as `vm_asm_out.txt`
```
700072000550005100B2B0C060520054530055B17000A00173001D7001770006790015B3B05000A1A0017000B0B3B17900055000B2B0540054550055B1B3B2B0711072004EB050007000B172000B700078000B910000
```
Using the command
```
python3 -m hackdecomp 5 0 < ./vm_asm_out.txt > ./decomp.txt
```
The output given by Hackdecomp should be
```
0x0005		LDX	0x00
0x0007		LDY	0x00
0x0009		PUSHY
0x000a		PUSHX
0x000b		RMEMX
0x000c		OUT
0x000d		STRX	0x0054
0x0010		STRY	0x0055
0x0013		POPX
0x0014		CMPX	0x00
0x0016		ADDX	0x01
0x0018		JRE	0x001d
0x001b		CMPX	0x01
0x001d		JRLE	0x0006
0x0020		JRG	0x0015
0x0023		POPY
0x0024		PUSHX
0x0025		LDX	0x00
0x0027		ADDXY
0x0028		ADDX	0x01
0x002a		CMPX	0x00
0x002c		PUSHX
0x002d		POPY
0x002e		POPX
0x002f		JRG	0x0005
0x0032		LDX	0x00
0x0034		PUSHY
0x0035		PUSHX
0x0036		LDRX	0x0054
0x0039		LDRY	0x0055
0x003c		POPX
0x003d		POPY
0x003e		PUSHY
0x003f		PUSHX
0x0040		CMPY	0x10
0x0042		JE	0x004e
0x0045		PUSHX
0x0046		LDX	0x00
0x0048		CMPX	0x00
0x004a		POPX
0x004b		JE	0x000b
0x004e		CMPX	0x00
0x0050		JG	0x000b
0x0053		RET
0x0054		0x00
0x0055		0x00
```

## License
Hackdecomp is licensed under the GPL v3 license. See [LICENSE](LICENSE) for details

## Notes
VM-O-MATIC and the accompanying specifications are proprietary software developed by [Sorint.lab S.p.A.](https://www.sorint.com/en/) for the [HackersGen Event](https://s4s.sorint.it/). Hackdecomp is in **NO WAY** affiliated with Sorint.lab S.p.A. and **IS NOT** a redistribution of software developed by Sorint.lab S.p.A. Hackdecomp has been developed solely by means of reverse engineering and official documentation by Sorint.lab S.p.A.
and is not intended to infringe Sorint.lab S.p.A.'s Intellectual Property. If you're a representatvie from Sorint.lab S.p.A. and would prefer for this project to be taken down, contact me at the E-Mail Address in my info box.

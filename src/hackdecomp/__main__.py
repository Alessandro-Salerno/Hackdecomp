import math
import sys


class VmInstructionInfo:
    def __init__(self, opcode: str, hasarg=True, argsize=1, maxarg=None) -> None:
        self.opcode = opcode
        self.hasarg = hasarg
        self.argsize = argsize
        self.maxarg = maxarg
        if self.maxarg == None:
            self.maxarg = int(math.pow(2, 8 * self.argsize))


VM_INSTRUCTIONS = {
    "40": VmInstructionInfo(opcode="CLD", hasarg=False, argsize=0),
    "50": VmInstructionInfo(opcode="LDX", hasarg=True, argsize=1),
    "51": VmInstructionInfo(opcode="LDY", hasarg=True, argsize=1),
    "52": VmInstructionInfo(opcode="STRX", hasarg=True, argsize=2, maxarg=4096),
    "53": VmInstructionInfo(opcode="STRY", hasarg=True, argsize=2, maxarg=4096),
    "54": VmInstructionInfo(opcode="LDRX", hasarg=True, argsize=2, maxarg=4096),
    "55": VmInstructionInfo(opcode="LDRY", hasarg=True, argsize=2, maxarg=4096),
    "60": VmInstructionInfo(opcode="OUT", hasarg=False, argsize=0, maxarg=4096),
    "61": VmInstructionInfo(opcode="IN", hasarg=False, argsize=0),
    "70": VmInstructionInfo(opcode="CMPX", hasarg=True, argsize=1),
    "71": VmInstructionInfo(opcode="CMPY", hasarg=True, argsize=1),
    "72": VmInstructionInfo(opcode="JE", hasarg=True, argsize=2),
    "73": VmInstructionInfo(opcode="JRE", hasarg=True, argsize=2, maxarg=4096),
    "74": VmInstructionInfo(opcode="JL", hasarg=True, argsize=2, maxarg=4096),
    "75": VmInstructionInfo(opcode="JRL", hasarg=True, argsize=2, maxarg=4096),
    "76": VmInstructionInfo(opcode="JLE", hasarg=True, argsize=2, maxarg=4096),
    "77": VmInstructionInfo(opcode="JRLE", hasarg=True, argsize=2, maxarg=4096),
    "78": VmInstructionInfo(opcode="JG", hasarg=True, argsize=2, maxarg=4096),
    "79": VmInstructionInfo(opcode="JRG", hasarg=True, argsize=2, maxarg=4096),
    "7A": VmInstructionInfo(opcode="JGE", hasarg=True, argsize=2, maxarg=4096),
    "7B": VmInstructionInfo(opcode="JRGE", hasarg=True, argsize=2, maxarg=4096),
    "A0": VmInstructionInfo(opcode="ADDX", hasarg=True, argsize=1),
    "A1": VmInstructionInfo(opcode="ADDXY", hasarg=False, argsize=0),
    "A2": VmInstructionInfo(opcode="DECX", hasarg=True, argsize=1),
    "A3": VmInstructionInfo(opcode="DECXY", hasarg=False, argsize=0),
    "A4": VmInstructionInfo(opcode="RORX", hasarg=False, argsize=0),
    "A5": VmInstructionInfo(opcode="ROLX", hasarg=False, argsize=0),
    "A6": VmInstructionInfo(opcode="XORX", hasarg=False, argsize=0),
    "B0": VmInstructionInfo(opcode="PUSHX", hasarg=False, argsize=0),
    "B1": VmInstructionInfo(opcode="POPX", hasarg=False, argsize=0),
    "B2": VmInstructionInfo(opcode="PUSHY", hasarg=False, argsize=0),
    "B3": VmInstructionInfo(opcode="POPY", hasarg=False, argsize=0),
    "C0": VmInstructionInfo(opcode="RMEMX", hasarg=False, argsize=0),
    "C1": VmInstructionInfo(opcode="WMEMX", hasarg=False, argsize=0),
    "C2": VmInstructionInfo(opcode="RMEMY", hasarg=False, argsize=0),
    "C3": VmInstructionInfo(opcode="WMEMY", hasarg=False, argsize=0),
    "90": VmInstructionInfo(opcode="NOP", hasarg=False, argsize=0),
    "91": VmInstructionInfo(opcode="RET", hasarg=False, argsize=0)
}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR: Expected 2 arguments: start end")
        exit(-1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    code = input()

    i = start * 2
    end = end if end != 0 else len(code)
    bc = start
    while i < end - 1:
        opcode = code[i:i+2]
        if opcode not in VM_INSTRUCTIONS:
            print(f"0x{format(bc, '04x')}\t\t0x{format(int(opcode, 16), '02x')}")
            i += 2
            bc += 1
            continue

        inst = VM_INSTRUCTIONS[opcode]
        b = i + 2
        e = b + inst.argsize * 2
        args = code[b:e]
        if inst.argsize == 0:
            print(f"0x{format(bc, '04x')}\t\t{inst.opcode}")
        elif inst.argsize == 1:
            print(f"0x{format(bc, '04x')}\t\t{inst.opcode}\t0x{format(int(args, 16), '02x')}")
        elif inst.argsize == 2:
            print(f"0x{format(bc, '04x')}\t\t{inst.opcode}\t0x{format(int(args, 16), '04x')}")
        i += 2 + inst.argsize * 2
        bc += 1 + inst.argsize
    

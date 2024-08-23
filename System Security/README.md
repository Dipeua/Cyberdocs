Les protections de mémoire modernes 

- **DEP (Data Execution Prevention)**
- **ASLR (Address Space Layout Randomization)** 
- **Canarie**

# Registers

| X86 Naming Convention | Name                    | Purpose                                                                                                                                                              |
| --------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EAX                   | Accumulator             | Used in arthmetic operation                                                                                                                                          |
| ECX                   | Counter                 | Used in shift/rotate instruction and loops                                                                                                                           |
| EDX                   | Data                    | Used in arthmetic operation and I/O                                                                                                                                  |
| EBX                   | Base                    | Used as a pointer to data                                                                                                                                            |
| ==ESP==               | ==Stack Pointer==       | ==Pointer to the top of the stack==                                                                                                                                  |
| ==EBP==               | ==Base Pointer==        | ==Pointer to the base of the stack (aka Stack Pointer, or Frame pointer)==                                                                                           |
| ESI                   | Source Index            | Used as a pointer to source in stream operation                                                                                                                      |
| EDI                   | Destination             | Used as a pointer to destination in stream operation                                                                                                                 |
| ==EIP==               | ==Instruction Pointer== | ==Controls the program execution by storing a pointer to the address of the next instruction that will be executed: It tells the CPU where the next instruction is== |

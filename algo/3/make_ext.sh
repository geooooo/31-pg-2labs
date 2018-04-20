gcc -shared -Wl,-soname,adder -o dev/ograph.so -fPIC dev/ograph.c
cp dev/ograph.so build/ograph/ograph.so

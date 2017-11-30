
#build macosx
mkdir build_mac && cd build_mac

cmake \
    -DCMAKE_TOOLCHAIN_FILE=../cmakes/MACOSX.toolchain.cmake \
    ../../src

cd ..
cmake --build build_mac
#copy
rm -rf build_mac
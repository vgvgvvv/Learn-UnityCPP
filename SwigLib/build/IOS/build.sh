
#build ios
mkdir build_ios && cd build_ios

cmake \
    -DCMAKE_TOOLCHAIN_FILE=../cmakes/iOS.toolchain.cmake \
    ../../src

cd ..
cmake --build build_ios
#copy
rm -rf build_ios
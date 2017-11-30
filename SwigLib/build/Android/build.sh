
#build android x86
mkdir build_android_x86 && cd build_android_x86

cmake \
    -DCMAKE_TOOLCHAIN_FILE=../cmakes/android.toolchain.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DANDROID_ABI=x86 \
    -DANDROID_NATIVE_API_LEVEL=android-14 \
    ../../src

make -j8
#copy
cd ..
rm -rf build_android_x86

#build android armeabi-v7a
mkdir build_android_armeabi-v7a && cd build_android_armeabi-v7a
cmake ../../src

cmake \
    -DCMAKE_TOOLCHAIN_FILE=../cmakes/android.toolchain.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DANDROID_ABI=armeabi-v7a \
    -DANDROID_NATIVE_API_LEVEL=android-14 \
    ../../src

make -j8
#copy
cd ..
rm -rf armeabi-v7a
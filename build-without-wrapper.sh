#!/bin/bash
echo "Building without Gradle wrapper..."
# This is a fallback script
cd app
# Create minimal build.gradle if missing
if [ ! -f "build.gradle" ]; then
  cat > build.gradle << 'GRADLE_BUILD'
plugins {
    id 'com.android.application'
}

android {
    compileSdk 34
    namespace 'com.aiteacher.notebook'
    
    defaultConfig {
        applicationId "com.aiteacher.notebook"
        minSdk 24
        targetSdk 34
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
}
GRADLE_BUILD
fi

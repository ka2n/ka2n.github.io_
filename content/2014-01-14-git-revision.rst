gitのコミット回数をiOSのCFBundleVersionに設定する
==================================================
:date: 2014-01-14
:author: ka2n
:status: draft
:slug: git-commit-count-to-cfbundleversion

開発ディレクトリのInfo.plistではなくて、ビルド後のInfo.plistに書き込んだ方が吉

.. code-block:: bash

    #!/bin/bash
    git=`which git`
    buildNumber=$($git log --pretty=oneline | wc -l)
    buildNumber=$(expr $(echo $buildNumber) + 1352)
    plistPath="${BUILT_PRODUCTS_DIR}/${EXECUTABLE_NAME}.app/Info.plist"
    echo buildNumber: $buildNumber
    echo plistPath: $plistPath
    if [ -f "${plistPath}" ]; then
        /usr/libexec/PlistBuddy -c "Set :CFBundleVersion ${buildNumber}" "${plistPath}"
    else
        echo "Skipping versioning..."
    fi

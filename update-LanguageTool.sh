#!/bin/sh

echo "Checking LanguageTool"

LATEST="$(
   curl -s https://languagetool.org/download/ \
		| sed -n 's/^.*href="LanguageTool-\([0-9]*\.[0-9]*\)\.zip".*$/\1/p' \
		| tail -n1
	)"

echo "Latest version:  $LATEST"

PKG="$(
	grep ^Version: LanguageTool.spec \
		| awk '{print $2}'
	)"

echo "Package version: $PKG"

if [ "$LATEST" != "$PKG" ]; then
	DATE="$(date "+%a %b %d %Y")"
	USER="Lars Kiesow <lkiesow@uos.de>"
	sed -i "s/^\(Version: *\).*/\1${LATEST}/" LanguageTool.spec
	sed -i "s/^%changelog/%changelog\n\* ${DATE} ${USER} - ${LATEST}\n- Update to ${LATEST}\n/" LanguageTool.spec

	git commit LanguageTool.spec -m "Update LanguageTool to ${LATEST}"
	git push
fi

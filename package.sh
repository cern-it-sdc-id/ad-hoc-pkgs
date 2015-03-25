#!/bin/bash

if [[ "$1" == "" ]]; then
  echo "Usage $0 [spec]"
  exit 1
fi

SPEC=$1
RPMBUILD=`pwd`

set -x
rpmbuild --define "_sourcedir ${RPMBUILD}" \
  --define "_specdir ${RPMBUILD}" \
  --define "_builddir ${RPMBUILD}" \
  --define "_srcrpmdir ${RPMBUILD}" \
  --define "_rpmdir ${RPMBUILD}" \
  --nodeps -bs "${SPEC}"


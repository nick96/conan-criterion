# Copyright (C) 2018 ADLINK Technology
# Copyright (C) 2015-2016 Franklin "Snaipe" Mathieu.
# Redistribution and use of this file is allowed according to the terms of the MIT license.
# For details see the LICENSE file distributed with Criterion.

# - Find Nanopb
# Find the native Nanopb headers and libraries.
#
# CSPTR_INCLUDE_DIRS - where to find pb.h, etc.
# CSPTR_LIBRARIES - List of libraries when using Nanopb.
# CSPTR_FOUND - True if Nanopb has been found.

# Look for the header file.
FIND_PATH(NANOPB_INCLUDE_DIR pb.h)

# Look for the library.
FIND_LIBRARY(NANOPB_LIBRARY NAMES protobuf-nanopb)

# Handle the QUIETLY and REQUIRED arguments and set NANOPB_FOUND to TRUE if all listed variables are TRUE.
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(NANOPB DEFAULT_MSG NANOPB_LIBRARY NANOPB_INCLUDE_DIR)

# Copy the results to the output variables.
IF(NANOPB_FOUND)
    SET(NANOPB_LIBRARIES ${NANOPB_LIBRARY})
    SET(NANOPB_INCLUDE_DIRS ${NANOPB_INCLUDE_DIR})
ELSE(NANOPB_FOUND)
    SET(NANOPB_LIBRARIES)
    SET(NANOPB_INCLUDE_DIRS)
ENDIF(NANOPB_FOUND)

MARK_AS_ADVANCED(NANOPB_INCLUDE_DIRS NANOPB_LIBRARIES)

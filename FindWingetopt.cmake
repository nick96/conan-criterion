# Copyright (C) 2018 ADLINK Technology
# Copyright (C) 2015-2016 Franklin "Snaipe" Mathieu.
# Redistribution and use of this file is allowed according to the terms of the MIT license.
# For details see the LICENSE file distributed with Criterion.

# - Find Wingetopt
# Find the native wingetopt headers and libraries.
#
# CSPTR_INCLUDE_DIRS - where to find getopt.h, etc.
# CSPTR_LIBRARIES - List of libraries when using wingetopt.
# CSPTR_FOUND - True if wingetopt has been found.

# Look for the header file.
FIND_PATH(WINGETOPT_INCLUDE_DIR getopt.h)

# Look for the library.
FIND_LIBRARY(WINGETOPT_LIBRARY NAMES wingetopt)

# Handle the QUIETLY and REQUIRED arguments and set NANOPB_FOUND to TRUE if all listed variables are TRUE.
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WINGETOPT DEFAULT_MSG WINGETOPT_LIBRARY WINGETOPT_INCLUDE_DIR)

# Copy the results to the output variables.
IF(WINGETOPT_FOUND)
    SET(WINGETOPT_LIBRARIES ${WINGETOPT_LIBRARY} ${CONAN_LIBS_WINGETOPT})
    SET(WINGETOPT_INCLUDE_DIRS ${WINGETOPT_INCLUDE_DIR})
ELSE(WINGETOPT_FOUND)
    SET(WINGETOPT_LIBRARIES)
    SET(WINGETOPT_INCLUDE_DIRS)
ENDIF(WINGETOPT_FOUND)

MARK_AS_ADVANCED(WINGETOPT_INCLUDE_DIRS WINGETOPT_LIBRARIES)

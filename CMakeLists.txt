cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES NONE)

# Set in the current scope the following variables:
# - s5cmd_archive_url
# - s5cmd_archive_sha256
include(${CMAKE_CURRENT_SOURCE_DIR}/s5cmdUrls.cmake)

#
# Download & extract archive
#
set(download_dir "${PROJECT_BINARY_DIR}")
set(extract_dir "${PROJECT_BINARY_DIR}/s5cmd-binary-distribution")
include(FetchContent)
FetchContent_Populate(s5cmd
  URL ${s5cmd_archive_url}
  URL_HASH SHA256=${s5cmd_archive_sha256}
  DOWNLOAD_DIR ${download_dir}
  SOURCE_DIR "${extract_dir}"
  )

#
# Install executable
#
set(_permissions PERMISSIONS
  OWNER_READ OWNER_WRITE OWNER_EXECUTE
  GROUP_READ GROUP_EXECUTE
  WORLD_READ WORLD_EXECUTE
  )
set(executable_name "s5cmd${CMAKE_EXECUTABLE_SUFFIX}")
install(PROGRAMS ${extract_dir}/${executable_name} DESTINATION "s5cmd/bin" ${_permissions})

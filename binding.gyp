{
  "targets": [
    {
      "target_name": "binding",
      "sources": [ "src/binding.cc",
                   "deps/libsnappy/snappy.cc",
                   "deps/libsnappy/snappy-sinksource.cc"
      ],
      "cflags": [
        "-O3",
        "-DNDEBUG",
        "-D_FILE_OFFSET_BITS=64",
        "-D_LARGEFILE_SOURCE" ]
    }
  ]
}

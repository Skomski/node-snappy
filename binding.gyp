{
  "targets": [
    {
      "target_name": "binding",
      "sources": [ "src/binding.cc",
                   "deps/snappy-1.1.0/snappy.cc",
                   "deps/snappy-1.1.0/snappy-sinksource.cc"
      ],
      "cflags": [
        "-O3",
        "-DNDEBUG",
        "-D_FILE_OFFSET_BITS=64",
        "-D_LARGEFILE_SOURCE" ]
    }
  ]
}

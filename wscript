import os
import Options
import Utils

srcdir = '.'
blddir = 'build'
VERSION = '0.0.2'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

  Utils.exec_command('./configure', cwd = './deps/libsnappy')

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.cxxflags = ['-Wall', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE']
  obj.target = 'binding'
  obj.source = 'src/binding.cc deps/libsnappy/snappy.cc deps/libsnappy/snappy-sinksource.cc'
  obj.includes = 'deps/libsnappy/'
  obj.install_path = None

def test(tsk):
  Utils.exec_command('node test/test.js')

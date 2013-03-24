require 'rubygems'
require 'slim'
require 'yaml'
require 'albino'
require 'fileutils'
require 'rcodetools/xmpfilter'
require 'open3'
require 'json'


$:.unshift File.dirname(__FILE__) + '/slides'

autoload :Example,     'example'
autoload :Annotate,    'annotate'
autoload :Annotator,   'annotator'
autoload :List,        'list'
autoload :SlideHelper, 'slide_helper'
autoload :Lecture,     'lecture'
autoload :Builder,     'builder'

Slim::Engine.default_options[:disable_escape] = true

Slim::EmbeddedEngine.register :example, Example
Slim::EmbeddedEngine.register :annotate, Annotate
Slim::EmbeddedEngine.register :list, List

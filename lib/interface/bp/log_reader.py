#!/usr/bin/python
# -*-coding:UTF-8 -*-
"""
log读取

 __author__ = 'zsw'

"""
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import avro.io
import avro.schema
import os


def read_log(topic, log):
    schema = avro.schema.parse(open(os.path.abspath(os.path.dirname(__file__)) + "/avro_schema/" + topic + ".avsc").read())
    print "schema:", schema
    writer = DataFileWriter(open(os.path.abspath(os.path.dirname(__file__)) + topic + ".avro", "w"), DatumWriter(), schema)
    for i in range(5):
        writer.append(log)
    writer.close()
    reader = DataFileReader(open(os.path.abspath(os.path.dirname(__file__)) + topic + ".avro", "r"), DatumReader())
    for log in reader:
        print log



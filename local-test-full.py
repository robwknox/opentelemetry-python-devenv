from opentelemetry import metrics, trace
from opentelemetry.exporter.zipkin import ZipkinSpanExporter
from opentelemetry.exporter.zipkin.encoder import Encoding
from opentelemetry.exporter.zipkin.encoder.v1.json import JsonV1Encoder
# from opentelemetry.exporter.zipkin.encoder.v1.thrift import ThriftEncoder
from opentelemetry.exporter.zipkin.encoder.v2.json import JsonV2Encoder
from opentelemetry.exporter.zipkin.encoder.v2.protobuf import ProtobufEncoder
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchExportSpanProcessor,
    ConsoleSpanExporter,
    SimpleExportSpanProcessor
)
from thrift.Thrift import TType
from thrift.transport.TTransport import TMemoryBuffer
from thrift.protocol import TBinaryProtocol
import random
from opentelemetry.trace.ids_generator import RandomIdsGenerator
# from opentelemetry.exporter.zipkin.encoder.v1.thrift import ThriftRandomIdsGenerator
from struct import pack, unpack
import sys
import time
import ipaddress

if __name__ == '__main__':

    headers = "a=b"
    print(headers)
    print("headers: '", headers, "'")

    headers_dict = {}
    for header in headers.split(","):
        for header_parts in header.split("="):
            if len(header_parts) == 2:
                headers_dict[header_parts[0]] = header_parts[1]
            else:
                print(
                    "Invalid OTLP exporter header skipped: %r" % header
                )
    print(headers_dict)
    exit(0)

    #
    # metrics.set_meter_provider(MeterProvider())
    # metrics.get_meter_provider().

    trace.set_tracer_provider(TracerProvider(
        # ids_generator=ThriftRandomIdsGenerator()
    ))
    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(
            ZipkinSpanExporter(
                "thrift",
                "http://host.docker.internal:9411/api/v1/spans",
                encoding=Encoding.V1_THRIFT
            ),

            # ZipkinSpanExporter(
            #     "protobuf",
            #     "http://host.docker.internal:9411/api/v2/spans",
            #     encoding=Encoding.V2_PROTOBUF,
            #     local_node_ipv4="192.168.0.1",
            #     local_node_ipv6="2001:db8::c001",
            #     local_node_port=41412,
            # ),

            # ZipkinSpanExporter(
            #     "json-v2",
            #     "http://host.docker.internal:9411/api/v2/spans",
            #     local_node_ipv4="192.168.0.1",
            #     local_node_ipv6="2001:db8::c001",
            #     local_node_port=41412,
            # ),

            # ZipkinSpanExporter(
            #     "json-v1",
            #     "http://host.docker.internal:9411/api/v1/spans",
            #     encoding=Encoding.V1_JSON,
            #     local_node_ipv4="192.168.0.1",
            #     local_node_ipv6="2001:db8::c001",
            #     local_node_port=41412,
            # ),
        )
    )

    provider = trace.get_tracer_provider()
    tracer = trace.get_tracer(__name__, "1.1r")

    with tracer.start_as_current_span("foo") as foo_span:
        foo_span.add_event("Alpha")
        foo_span.add_event("boom boom")
        foo_span.set_attribute("phone", "iphone X")
        foo_span.set_attribute("beats", "spotify")
        with tracer.start_as_current_span("bar") as bar_span:
            bar_span.add_event("Apocalypse")
            bar_span.set_attribute("sky", "blue")
            with tracer.start_as_current_span("baz") as baz_span:
                baz_span.add_event("event 1")
                baz_span.set_attribute('att1', 'att_val1')

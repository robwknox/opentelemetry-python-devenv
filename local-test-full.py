from opentelemetry import trace
from opentelemetry.exporter.zipkin import ZipkinSpanExporter
from opentelemetry.exporter.zipkin.encoder import Encoding
from opentelemetry.exporter.zipkin.encoder.v1.json import JsonV1Encoder
from opentelemetry.exporter.zipkin.encoder.v1.thrift import ThriftEncoder
from opentelemetry.exporter.zipkin.encoder.v2.json import JsonV2Encoder
from opentelemetry.exporter.zipkin.encoder.v2.protobuf import ProtobufEncoder
from opentelemetry.exporter.zipkin.endpoint import Endpoint
from opentelemetry.sdk.resources import Resource
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
from opentelemetry.exporter.zipkin.encoder.v1.thrift import ThriftRandomIdsGenerator
from struct import pack, unpack
import sys
import time

if __name__ == '__main__':

    trace.set_tracer_provider(TracerProvider(
        # ids_generator=ThriftRandomIdsGenerator()
    ))
    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(
            ZipkinSpanExporter(
                "thrift",
                "http://host.docker.internal:9411/api/v1/spans",
                encoding=Encoding.THRIFT
            ),
            #
            # ZipkinSpanExporter(
            #     "protobuf",
            #     "http://host.docker.internal:9411/api/v2/spans",
            #     encoding=Encoding.PROTOBUF,
            #     encoder=ProtobufEncoder(
            #         Endpoint(
            #             "protobuf-2",
            #             ipv4="192.168.0.1",
            #             ipv6="2001:db8::c001",
            #             port=41412
            #         )
            #     )
            # ),

            # ZipkinSpanExporter(
            #     endpoint="http://host.docker.internal:9411/api/v2/spans",
            #     encoder=JsonV2Encoder(
            #         Endpoint(
            #             "json-v2",
            #             ipv4="192.168.0.1",
            #             ipv6="2001:db8::c001",
            #             port=41412
            #         ),
            #     ),
            # ),
            #
            # ZipkinSpanExporter(
            #     endpoint="http://host.docker.internal:9411/api/v1/spans",
            #     encoder=JsonV1Encoder(
            #         Endpoint(
            #             "json-v1",
            #             ipv4="192.168.0.1",
            #             # ipv6="2001:db8::c001",
            #             port=41412
            #         ),
            #     ),
            #     encoding=Encoding.JSON_V1
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

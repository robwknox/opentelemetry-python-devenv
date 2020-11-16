from opentelemetry import trace
from opentelemetry.exporter.otlp.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.zipkin import ZipkinSpanExporter
from opentelemetry.exporter.zipkin.encoder import Encoding
from opentelemetry.exporter.zipkin.endpoint import Endpoint
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchExportSpanProcessor,
    ConsoleSpanExporter,
    SimpleExportSpanProcessor
)
from thrift.transport.TTransport import TMemoryBuffer
from thrift.protocol import TBinaryProtocol
from thrift.protocol import T
import random
from opentelemetry.trace.ids_generator import RandomIdsGenerator
from struct import pack

if __name__ == '__main__':

    #
    # gen = RandomIdsGenerator()
    #
    # # for iter in range(1, 128):
    #     # gen_id = gen.generate_trace_id()
    # gen_id = gen.generate_span_id()
    # print(type(gen_id))
    # print(f'{gen_id:40d} | {gen_id.bit_length():3d} | {bin(gen_id):128s}')
    # packed = pack("!q", gen_id)
    #
    #
    # exit(0)
    #

    #
    # print("37 : ", bin(-37), " : ", bin(-37).lstrip('-0b'))
    # print("37 : ", bin(37), " : ", bin(37).lstrip('-0b'))
    #
    # txt = ",,,,,ssaaww.....banana"
    #
    # print(txt, " : ", txt.lstrip(",.asw"))
    #
    # exit(0)
    #

    # for iter in range(1, 128):
    #     rand_num = random.getrandbits(iter)
    #     print(iter, " : ", rand_num.bit_length(), " : ", rand_num)
    #
    # exit(0)


    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(
            ZipkinSpanExporter(
                "thrift",
                "http://host.docker.internal:9411/api/v1/spans",
                encoding=Encoding.THRIFT
            ),
            # ZipkinSpanExporter(
            #     "protobuf",
            #     "http://host.docker.internal:9411/api/v2/spans",
            #     encoding=Encoding.PROTOBUF
            # ),
            # ZipkinSpanExporter(
            #     "json-v2", "http://host.docker.internal:9411/api/v2/spans",
            # ),
            # ZipkinSpanExporter(
            #     "json-v1",
            #     "http://host.docker.internal:9411/api/v1/spans",
            #     encoding=Encoding.JSON_V1
            # ),
            # ZipkinSpanExporter(
            #     LocalEndpoint(
            #         "json",
            #         "http://host.docker.internal:9411/api/v2/spans",
            #     ),
            #     transport_format=TransportFormat.V2_JSON
            # ),
            # ZipkinSpanExporter(
            #     LocalEndpoint(
            #         "json-v1",
            #         "http://host.docker.internal:9411/api/v1/spans",
            #     ),
            #     transport_format=TransportFormat.V1_JSON
            # ),
            # OTLPSpanExporter(endpoint="host.docker.internal:55681", insecure=True, timeout=3),
            # ConsoleSpanExporter(),
        )
    )

    # trace.get_tracer_provider().add_span_processor(
    #     SimpleExportSpanProcessor(
    #         ZipkinSpanExporter("rob-j", "http://host.docker.internal:9411/api/v2/spans", encoder=TransportFormat.V2_JSON),
    #         # ZipkinSpanExporter("rob", "http://host.docker.internal:9411/api/v2/spans", encoder=TransportFormat.V2_JSON),
    #         # OTLPSpanExporter(endpoint="host.docker.internal:55681", insecure=True, timeout=3),
    #         # ConsoleSpanExporter(),
    #     )
    # )

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

    eadlwij = 1
    # sleep(500)

    #
    # trace.set_tracer_provider(TracerProvider())
    # trace.get_tracer_provider().add_span_processor(
    #     SimpleExportSpanProcessor(ConsoleSpanExporter())
    # )
    #
    #
    #
    # with tracer.start_as_current_span("foo"):
    #     with tracer.start_as_current_span("bar"):
    #         with tracer.start_as_current_span("baz") as baz_span:
    #             baz_span.add_event("event 1")
    #             baz_span.set_attribute('att1', 'att_val1')
    #             print("Hello world from OpenTelemetry Python!")

from grpc import insecure_channel

from opentelemetry import trace
from opentelemetry.exporter.otlp import Protocol, Compression
from opentelemetry.exporter.otlp.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.sender.grpc import _load_credential_from_file
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchExportSpanProcessor,
    SimpleExportSpanProcessor
)

if __name__ == '__main__':

    # file = _load_credential_from_file("/root/service.pem")
    # a = 1
    # exit(0)
    # channel = insecure_channel("host.docker.internal:55680")

    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        BatchExportSpanProcessor(
            OTLPSpanExporter(
                "host.docker.internal:55680",
                # insecure=True,
                # compression=Compression.NONE,
                # headers="rob=testing",
                cert_file="/root/ca.crt"
            )
        )
        #
        # BatchExportSpanProcessor(
        #     OTLPSpanExporter(
        #         protocol=Protocol.HTTP_PROTOBUF,
        #         endpoint="http://host.docker.internal:55681/v1/traces",
        #         insecure=True,
        #         compression=Compression.DEFLATE,
        #     )
        # )
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

    print("done")

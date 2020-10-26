from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor
)

import json

if __name__ == '__main__':

    print('PyCharm')

    test = []
    if test:
        print("pass 1")

    test.append('a')

    if test:
        print("pass 2")

    # trace.set_tracer_provider(TracerProvider())
    # trace.get_tracer_provider().add_span_processor(
    #     SimpleExportSpanProcessor(ConsoleSpanExporter())
    # )
    #
    # tracer = trace.get_tracer(__name__)
    #
    # with tracer.start_as_current_span("foo"):
    #     with tracer.start_as_current_span("bar"):
    #         with tracer.start_as_current_span("baz") as baz_span:
    #             baz_span.add_event("event 1")
    #             baz_span.set_attribute('att1', 'att_val1')
    #             print("Hello world from OpenTelemetry Python!")

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor
)

if __name__ == '__main__':
    print('PyCharm')

    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(ConsoleSpanExporter())
    )

    tracer = trace.get_tracer(__name__)

    # rob_span = tracer.start_span("rob")
    # rob_span.add_event("event 1", {"att1": "val1"})
    # rob_span.set_attribute('att1', 'att_val1')
    # rob_span.end()

    # span = tracer.start_span("rob")
    # with tracer.use_span(span, end_on_exit=True):
    #     print("hi")

    # with tracer.start_as_current_span("rob") as span:
    #     span.add_event("event 1", {"att1": "val1"})
    #     span.set_attribute('att1', 'att_val1')
    #     print("hi")

    with tracer.start_as_current_span("foo"):
        with tracer.start_as_current_span("bar"):
            with tracer.start_as_current_span("baz") as baz_span:
                baz_span.add_event("event 1")
                baz_span.set_attribute('att1', 'att_val1')
                print("Hello world from OpenTelemetry Python!")

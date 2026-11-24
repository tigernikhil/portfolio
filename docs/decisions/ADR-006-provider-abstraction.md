# ADR-006: Provider Abstraction

## Context

The Personal Technology Platform (PTP) interacts with various external services and infrastructure components such as databases, message queues, and APIs. To maintain a clean separation of concerns, adhere to the Dependency Inversion Principle, and facilitate easier testing and maintenance, we need to implement a ports and adapters architecture for all external infrastructure.

## Decision

We will use the Hexagonal Architecture (also known as Ports and Adapters) pattern to decouple the platform's internal business rules from external concerns. This approach promotes loose coupling, high cohesion, and easier maintenance and testing.

## Consequences

### Structure

The platform will be structured as follows:

- **Domain**: Contains the core business logic, entities, value objects, and domain events.
- **Application**: Contains use cases and services that orchestrate domain objects.
- **Infrastructure**: Contains ports (interfaces) and adapters (implementations) for external infrastructure.

### Ports and Adapters

#### Ports (Interfaces)

- **Repositories**: Interfaces for data persistence (e.g., `UserRepository`, `TaskRepository`).
- **Message Brokers**: Interfaces for publishing and consuming messages (e.g., `TaskCreatedEventPublisher`, `TaskUpdatedEventSubscriber`).
- **API Clients**: Interfaces for communicating with external APIs (e.g., `GoogleCalendarClient`, `SlackClient`).

#### Adapters (Implementations)

- **Repositories**:
  - In-memory: For testing and development purposes.
  - Database: For production use, implementing specific database technologies (e.g., PostgreSQL, MongoDB).
  - Caching: Implementing caching strategies to improve performance.

| Repository | In-memory | Database | Caching |
|---|---|---|---|
| UserRepository | ✅ | ✅ | ✅ |
| TaskRepository | ✅ | ✅ | ✅ |

- **Message Brokers**:
  - RabbitMQ: Implementing RabbitMQ as the message broker.
  - In-memory: For testing and development purposes.

| Message Broker | RabbitMQ | In-memory |
|---|---|---|
| TaskCreatedEventPublisher | ✅ | ✅ |
| TaskUpdatedEventSubscriber | ✅ | ✅ |

- **API Clients**:
  - Google Calendar: Implementing the Google Calendar API.
  - Slack: Implementing the Slack API.
  - In-memory: For testing and development purposes.

| API Client | Google Calendar | Slack | In-memory |
|---|---|---|---|
| GoogleCalendarClient | ✅ |  | ✅ |
| SlackClient |  | ✅ | ✅ |

### Testing

With this architecture, testing becomes easier as the domain and application layers are decoupled from external dependencies. This allows for unit testing of domain and application objects in isolation.

### Maintenance and Evolution

The ports and adapters architecture promotes easier maintenance and evolution of the platform. Changes in external infrastructure can be handled by updating the corresponding adapter without affecting the domain and application layers. Additionally, adding new external services or replacing existing ones becomes simpler as it only requires implementing a new adapter or updating an existing one.

## Status

Accepted

## References

- [Hexagonal Architecture](https://alistair.cockburn.us/Hexagonal+Architecture)
- [Ports and Adapters](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

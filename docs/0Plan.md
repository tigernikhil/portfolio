Personal Technology Platform — Complete Engineering Blueprint
Project location: /Users/admin/Downloads/Portfolio

Objective: Build a beautiful, secure, dynamic and extensible platform that combines your professional portfolio, public tools, private applications, AI capabilities, MCP integrations and developer utilities.

The platform must support multiple coding agents and allow infrastructure providers, tools and integrations to be replaced without rewriting the entire application.

This is the complete implementation blueprint, from initial discovery through production release.

1. Product vision
Build one central platform with four major areas.
Personal Technology Platform

One identity · Multiple applications · Centralized management

Portfolio

Experience, projects, achievements and technical articles.


Tools directory

Public and private applications with searchable capabilities.


Private workspace

Login, permissions, personal utilities and restricted tools.


AI & Developer platform

LLMs, MCP, APIs, automation and local models.




User types
User	Capabilities
Visitor	Browse portfolio and public tools
Registered user	Use authenticated tools
Invited user	Use specifically authorized private tools
Administrator	Manage users, tools and projects
Owner	Full platform administration

Core functionality
Public website
- Homepage.
- About/profile.
- Professional experience.
- Project portfolio.
- Tools directory.
- Individual tool pages.
- Public tool execution.
- Contact form.
- Engineering blog.
- SEO.
Authentication
- Registration.
- Login/logout.
- Email verification.
- Password recovery.
- Secure sessions.
- MFA for administrators.
- User suspension.
- Account deletion.
Private workspace
- User dashboard.
- Available tools.
- Favorites.
- Execution history.
- Notifications.
- Profile settings.
Tool management
- Add and publish tools.
- Change visibility.
- Manage tool versions.
- Grant/revoke permissions.
- Configure execution.
- Monitor tool health.
- Track usage.
Administration
- User management.
- Role management.
- Tool management.
- Portfolio management.
- Integration management.
- Audit logs.
- Monitoring.
- Platform configuration.

2. Engineering constitution — mandatory policies
Every developer and coding agent must follow these rules.
Architecture policies
1. Use modular architecture.
2. Keep business logic independent of infrastructure.
3. Use interfaces for external providers.
4. Avoid circular dependencies.
5. Do not introduce microservices without justification.
6. Define contracts before implementing integrations.
7. Use independent execution environments for tools that need them.
8. Keep all major architectural decisions documented.
Replaceability policy
Every external dependency must have an adapter.
Capability	Initial provider	Possible replacement
Database	PostgreSQL / Supabase	Another PostgreSQL host
Authentication	Supabase Auth	OIDC provider
Email	Resend	SES, Postmark, SMTP
Storage	Supabase Storage	S3, R2, MinIO
Queue	Cloudflare Queues	SQS, RabbitMQ
AI	Ollama / API providers	Other compatible LLMs
Hosting	Cloudflare	Other compatible runtime
Logging	OpenTelemetry	Other telemetry backend
Tool execution	Runtime adapters	Worker, API, container

Important: Replaceability requires explicit contracts and migration plans. A database or identity provider cannot always be swapped with a simple configuration change.
Code quality policies
Area	Standard
Language	TypeScript strict
Formatting	Prettier
Linting	ESLint
Validation	Zod
Unit testing	Vitest
E2E testing	Playwright
API documentation	OpenAPI
Database changes	Version-controlled migrations
Package manager	pnpm
Git workflow	Feature branches and pull requests

Mandatory rules
- No secrets in Git.
- No business logic in React components.
- No direct database calls from UI components.
- No frontend-only authorization.
- No untrusted code execution in the main application.
- No destructive database migrations without approval.
- No undocumented breaking changes.
- No claiming tests passed without executing them.
Definition of Done
Every feature must have:
- Requirements.
- Acceptance criteria.
- Implementation.
- Unit and integration tests as applicable.
- Authorization checks.
- Error handling.
- Loading and empty states.
- Accessibility validation.
- Documentation.
- Successful CI checks.

3. Technology stack
Recommended stack










Next.js + TypeScript

Frontend, routing, server-side application













Cloudflare Workers

Hosting, edge execution, APIs













Supabase + PostgreSQL

Database, authentication, storage













Resend

Transactional emails and notifications













GitHub

Version control and CI/CD



Additional selections:
- Tailwind CSS + shadcn/ui.
- Radix UI.
- React Hook Form.
- Zod.
- Drizzle ORM.
- Vitest.
- Playwright.
- OpenTelemetry.
- Cloudflare Queues.
- Ollama and external LLM APIs.
Hosting consideration: Validate Next.js compatibility with the selected Cloudflare deployment adapter before freezing it. Keep application logic portable to a standard Node.js runtime.

4. System architecture
Recommended architecture:

Modular monolith + ports and adapters + independent tool execution services.

The main platform should not start with dozens of microservices.
#chatgpt-mermaid-_r_2da_{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:14px;fill:rgb(255, 255, 255);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_2da_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_2da_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_2da_ .error-icon{fill:rgba(255, 255, 255, 0.03);}#chatgpt-mermaid-_r_2da_ .error-text{fill:rgb(255, 255, 255);stroke:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_2da_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_2da_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_2da_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_2da_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_2da_ .marker{fill:rgba(255, 255, 255, 0.498);stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2da_ .marker.cross{stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2da_ svg{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:14px;}#chatgpt-mermaid-_r_2da_ p{margin:0;}#chatgpt-mermaid-_r_2da_ .label{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ .cluster-label text{fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ .cluster-label span{color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_2da_ .label text,#chatgpt-mermaid-_r_2da_ span{fill:rgb(255, 255, 255);color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ .node rect,#chatgpt-mermaid-_r_2da_ .node circle,#chatgpt-mermaid-_r_2da_ .node ellipse,#chatgpt-mermaid-_r_2da_ .node polygon,#chatgpt-mermaid-_r_2da_ .node path{fill:rgb(26, 40, 61);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .rough-node .label text,#chatgpt-mermaid-_r_2da_ .node .label text,#chatgpt-mermaid-_r_2da_ .image-shape .label,#chatgpt-mermaid-_r_2da_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_2da_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .rough-node .label,#chatgpt-mermaid-_r_2da_ .node .label,#chatgpt-mermaid-_r_2da_ .image-shape .label,#chatgpt-mermaid-_r_2da_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_2da_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_2da_ .root .anchor path{fill:rgba(255, 255, 255, 0.498)!important;stroke-width:0;stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2da_ .arrowheadPath{fill:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2da_ .edgePath .path{stroke:rgba(255, 255, 255, 0.498);stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .flowchart-link{stroke:rgba(255, 255, 255, 0.498);fill:none;}#chatgpt-mermaid-_r_2da_ .edgeLabel{background-color:rgb(24, 24, 24);text-align:center;}#chatgpt-mermaid-_r_2da_ .edgeLabel p{background-color:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2da_ .edgeLabel rect{opacity:0.5;background-color:rgb(24, 24, 24);fill:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2da_ .labelBkg{background-color:rgba(24, 24, 24, 0.5);}#chatgpt-mermaid-_r_2da_ .cluster rect{fill:rgba(255, 255, 255, 0.03);stroke:rgba(255, 255, 255, 0.082);stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .cluster text{fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ .cluster span{color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:12px;background:rgba(255, 255, 255, 0.03);border:1px solid rgba(255, 255, 255, 0.082);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_2da_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2da_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_2da_ .icon-shape,#chatgpt-mermaid-_r_2da_ .image-shape{background-color:rgb(24, 24, 24);text-align:center;}#chatgpt-mermaid-_r_2da_ .icon-shape p,#chatgpt-mermaid-_r_2da_ .image-shape p{background-color:rgb(24, 24, 24);padding:2px;}#chatgpt-mermaid-_r_2da_ .icon-shape .label rect,#chatgpt-mermaid-_r_2da_ .image-shape .label rect{opacity:0.5;background-color:rgb(24, 24, 24);fill:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2da_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_2da_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_2da_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_2da_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_2da_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_2da_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_2da_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2da_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_2da_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_2da_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_2da_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2da_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_2da_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_2da_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2da_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_2da_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_2da_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2da_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_2da_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2da_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_2da_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_2da_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_2da_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_2da_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .node rect,#chatgpt-mermaid-_r_2da_ .node circle,#chatgpt-mermaid-_r_2da_ .node ellipse,#chatgpt-mermaid-_r_2da_ .node polygon,#chatgpt-mermaid-_r_2da_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_2da_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_2da_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_2da_ .edgePaths .flowchart-link{stroke:rgba(255, 255, 255, 0.498);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_2da_ .marker{fill:rgba(255, 255, 255, 0.498);stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2da_ :root{--mermaid-font-family:-apple-system,"system-ui","Segoe UI",sans-serif;}Tool RuntimesInfrastructureDomain LayerApplicationCloudflare WorkersExternal APIsMCP ServersLocal AI GatewayPostgreSQLEmailObject StorageJob QueueAI ProvidersIdentity and PermissionsTool ManagementProject ManagementExecution ManagementPublic WebsiteAuthenticationWorkspaceAdmin DashboardTool RegistryExecution RouterVisitors and Registered UsersCloudflare EdgeNext.js Application





Layer responsibilities
Layer	Responsibility
Presentation	Pages, components and user interactions
Application	Use cases and orchestration
Domain	Business rules and entities
Infrastructure	Database, email, storage, queues
Tool runtime	Execute independently registered tools

The domain layer must not import Next.js, Supabase or Cloudflare SDKs.

5. Repository structure
Recommended monorepo:
Portfolio/
│
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .env.example
│
├── apps/
│   ├── web/
│   ├── worker-runtime/
│   ├── background-worker/
│   └── mcp-gateway/
│
├── packages/
│   ├── domain/
│   ├── application/
│   ├── contracts/
│   ├── database/
│   ├── identity/
│   ├── authorization/
│   ├── tool-registry/
│   ├── tool-sdk/
│   ├── tool-runtime/
│   ├── storage/
│   ├── email/
│   ├── queue/
│   ├── ai-providers/
│   ├── observability/
│   ├── ui/
│   └── testing/
│
├── tools/
│   ├── finance/
│   ├── productivity/
│   ├── ai/
│   ├── developer/
│   └── automation/
│
├── infrastructure/
│   ├── cloudflare/
│   ├── database/
│   ├── scripts/
│   └── deployment/
│
├── supabase/
│   ├── migrations/
│   └── seed.sql
│
├── docs/
│   ├── product/
│   ├── architecture/
│   ├── design/
│   ├── security/
│   ├── database/
│   ├── api/
│   ├── integrations/
│   ├── testing/
│   ├── operations/
│   ├── deployment/
│   ├── release/
│   ├── roadmap/
│   └── decisions/
│
├── scripts/
├── tests/
├── pnpm-workspace.yaml
└── package.json


Dependency direction
Presentation
     |
     v
Application
     |
     v
Domain

Infrastructure Adapters
     |
     v
Contracts / Interfaces


Business logic should not depend on vendor implementations.

6. UI/UX design system
Visual direction
Create a premium developer-platform experience inspired by:
- Linear's clarity.
- Vercel's minimalism.
- Raycast's tool discovery.
- Stripe's documentation quality.
Do not copy these interfaces.
Design requirements
- Dark and light themes.
- Consistent typography.
- Restrained accent colours.
- Consistent spacing.
- Responsive layouts.
- Subtle animation.
- Excellent loading states.
- Accessible forms.
- Keyboard navigation.
- Clear error states.
- Consistent iconography.
Avoid excessive gradients, unnecessary animations and inconsistent card layouts.
Design system components
components/
  ui/
    Button
    Input
    Select
    Dialog
    Dropdown
    Tooltip
    Tabs
    Badge
    Avatar
    Skeleton
    Toast
    DataTable

  layout/
    Navbar
    Footer
    Sidebar
    PageHeader
    Breadcrumbs

  tools/
    ToolCard
    ToolHeader
    ToolFilters
    ToolStatus
    ToolLaunchButton
    ToolExecutionPanel

  dashboard/
    StatCard
    ActivityFeed
    RecentTools


Website pages
Page	Function
/	Homepage
/about	Professional profile
/portfolio	Projects
/tools	Tool directory
/tools/[slug]	Individual tool
/workspace	User dashboard
/workspace/tools	Authorized tools
/admin	Admin dashboard
/login	Authentication
/register	Registration
/contact	Contact form

Target WCAG 2.2 AA accessibility.

7. Database design
Use PostgreSQL as the primary database.
Core tables
Table	Purpose
profiles	User profiles
roles	Platform roles
user_roles	User-role relationships
permissions	Permission definitions
role_permissions	Role permissions
projects	Portfolio projects
technologies	Technology catalogue
project_technologies	Project technology mapping
tools	Tool registry
tool_versions	Tool version history
tool_categories	Tool categories
tool_capabilities	Tool capabilities
tool_permissions	Individual access grants
tool_runs	Execution records
tool_run_events	Execution events
tool_favorites	User favorites
notifications	In-app notifications
audit_logs	Security and admin history

Example tool schema
CREATE TABLE tools (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category_id UUID,
    visibility TEXT NOT NULL,
    status TEXT NOT NULL,
    execution_type TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);


Database policies
- Use UUID primary keys.
- Use UTC timestamps.
- Enforce foreign keys.
- Use explicit indexes.
- Maintain migrations in Git.
- Enable RLS on user-accessible tables.
- Use JSONB only for genuinely flexible configuration.
- Keep sensitive documents out of logs.
- Maintain ownership for user-generated resources.
Example user-owned record policy:
CREATE POLICY profile_read_own
ON profiles
FOR SELECT
USING (id = auth.uid());


Every table needs policies appropriate to its data ownership and access model. Do not blindly apply the same policy everywhere.

8. Authentication and authorization
Roles
Role	Permissions
Owner	Complete platform control
Admin	Operational management
User	Standard registered access
Visitor	Public access only

Tool visibility
Visibility	Access
Public	Anyone
Authenticated	Registered users
Restricted	Explicitly authorized users
Private	Owner and explicitly authorized users

Authentication flows
Registration
1. User submits registration.
2. Validate input.
3. Apply rate limits.
4. Create account.
5. Send verification email.
6. Verify email.
7. Create profile.
8. Assign standard user role.
9. Redirect to workspace.
Authorization
Every private operation must verify access server-side.
interface AuthorizationService {
  can(
    principal: UserIdentity,
    action: string,
    resource: Resource
  ): Promise<boolean>;
}


Mandatory controls:
- Secure sessions.
- HTTP-only cookies.
- MFA for administrators.
- Protected role assignment.
- RLS.
- Server-side permission checks.
- Session revocation.
- Audit logs.
- Account suspension.
- No privilege escalation.
New registrations must never receive administrator or owner privileges automatically.

9. Dynamic tool registry and plugin architecture
This is the most important technical component.

The website must not hardcode individual tools.
Tool manifest
Every tool should expose a manifest.
{
  "schemaVersion": "1.0",
  "id": "finance.stock-pnl",
  "name": "Stock P&L Analyzer",
  "version": "1.0.0",
  "description": "Analyze stock profit and loss reports.",
  "category": "finance",
  "visibility": "authenticated",
  "execution": {
    "type": "api",
    "reference": "stock-pnl-service"
  },
  "capabilities": [
    "document-upload",
    "financial-analysis"
  ]
}


The actual manifest must also define validated input/output schemas, versioning and execution limits.

Do not allow users to submit arbitrary executable URLs.
Tool execution modes
Mode	Example
Embedded	Calculator
Edge	Lightweight parser
API	Existing Java application
Job	Video generation
MCP	Developer automation
Local	Ollama

Standard tool interface
interface ToolExecutor {
  execute(
    input: unknown,
    context: ToolExecutionContext
  ): Promise<ToolExecutionResult>;

  healthCheck(): Promise<HealthStatus>;
}


Tool lifecycle
Draft
  |
Validating
  |
Approved
  |
Published
  |
Disabled
  |
Deprecated
  |
Archived


Publishing requires successful validation, security review, permissions, health check and version identification.
Tool SDK
Create a common SDK containing:
- Manifest validation.
- Input/output validation.
- Authentication context.
- Authorization context.
- Structured logging.
- Error mapping.
- Execution tracing.
- Idempotency.
- File handling.
- Testing helpers.
This allows independently developed tools to integrate consistently.

10. API and integration architecture
Use REST with OpenAPI.

Example endpoints:
/api/v1/tools
/api/v1/tools/{slug}
/api/v1/tools/{slug}/execute
/api/v1/executions/{id}
/api/v1/projects
/api/v1/users/me
/api/v1/notifications

/api/v1/admin/users
/api/v1/admin/tools
/api/v1/admin/tools/{id}/publish
/api/v1/admin/tools/{id}/permissions
/api/v1/admin/audit-logs


Standard response:
{
  "success": true,
  "data": {},
  "meta": {
    "requestId": "request-id"
  }
}


API requirements:
- Request validation.
- Response validation.
- Pagination.
- Idempotency where appropriate.
- Rate limiting.
- Timeouts.
- Structured errors.
- Versioning.
- Authorization.
- OpenAPI documentation.
Use interfaces and adapters for every external provider


11. AI, MCP and local AI architecture
AI gateway
AI Gateway
  |
  ├── Model Registry
  ├── Provider Selection
  ├── Request Validation
  ├── Usage Tracking
  ├── Rate Limiting
  ├── Timeout Management
  └── Provider Adapters
        ├── Ollama
        ├── OpenAI-compatible
        ├── Anthropic
        └── Other providers


Provider interface:
interface LLMProvider {
  capabilities(): ProviderCapabilities;

  generate(
    request: LLMRequest
  ): Promise<LLMResponse>;
}


Explicitly model provider capabilities such as streaming, tool calling, image inputs and structured outputs.
MCP gateway
Platform
   |
MCP Gateway
   |
   ├── Server Registry
   ├── Authentication
   ├── Authorization
   ├── Tool Allowlist
   ├── Validation
   ├── Timeouts
   └── Audit Logging
          |
          ├── Approved MCP servers
          ├── Developer utilities
          └── Local MCP services


MCP must not replace the platform's authorization system.

Do not expose confidential Oracle code, logs, telemetry, credentials or internal endpoints.
Local AI
Public Platform
      |
Authenticated Gateway
      |
Private Network / Tailscale
      |
Local AI Gateway
      |
      ├── Ollama
      ├── Local Models
      └── Authorized MCP Servers


Never expose Ollama or MCP services directly to the public internet.

When the local machine is offline, display service unavailability instead of silently failing.

12. Security and privacy policy
Use defence in depth and a zero-trust approach.
Risk	Protection
Account takeover	MFA, secure sessions
Privilege escalation	Server-side role controls
Data leakage	RLS, ownership checks
SQL injection	Parameterized queries
XSS	Output encoding and sanitization
CSRF	Secure cookie/session strategy
SSRF	Outbound destination restrictions
Malicious uploads	Validation and isolated processing
API abuse	Rate limiting and quotas
Secret exposure	Managed secrets
MCP misuse	Allowlist and execution controls
Denial of service	Resource limits and throttling

File upload security
- Validate extension.
- Validate MIME.
- Validate file signature.
- Restrict file size.
- Use randomized storage names.
- Use private buckets.
- Use short-lived signed URLs.
- Scan files where feasible.
- Isolate processing.
- Delete temporary files.
- Define retention.
Sensitive financial documents
For Form 16, 26AS and Stock P&L:
- Do not retain documents by default.
- Avoid logging PAN or account information.
- Provide deletion controls.
- Encrypt retained data.
- Restrict access to document processing services.
- Minimize external AI provider exposure.
Release security gate
Mandatory release blocker
No release with unresolved critical or high-severity security issues, exposed secrets, broken authorization or unauthorized private tool execution.

13. Email and notification architecture
Use an EmailProvider abstraction.

Initial provider: Resend.

Potential replacements: SES, Postmark and SMTP.
Email events
- Registration verification.
- Password reset.
- Welcome email.
- User invitation.
- Access granted.
- Access revoked.
- Tool completion.
- Security alerts.
- Contact form notification.
Professional email
Initially, use your existing Gmail address and transactional email testing.

After buying a domain:
hello@yourdomain.com
support@yourdomain.com
notifications@yourdomain.com


Configure:
- SPF.
- DKIM.
- DMARC.
- Incoming email forwarding or a mailbox.
- Verified transactional sender.
Cloudflare Email Routing forwards incoming messages; it does not itself provide a full mailbox.

14. Background jobs and execution
Do not make users wait for long-running processing.

Use asynchronous jobs for:
- Large PDF processing.
- AI generation.
- Video generation.
- Bulk processing.
- Automation.
- External workflows.
User Request
    |
Authorization
    |
Create Job
    |
Queue
    |
Background Worker
    |
Tool Runtime
    |
Update Status
    |
Notify User


Job states:
CREATED
QUEUED
RUNNING
COMPLETED
FAILED
CANCELLED
TIMED_OUT


Mandatory features:
- Idempotency.
- Retry limits.
- Exponential backoff.
- Dead-letter handling.
- Timeouts.
- Cancellation.
- Progress updates.
- User concurrency limits.
Use Cloudflare Queues where compatible. Heavy GPU/CPU workloads should run separately.

15. Observability and operations
Implement structured JSON logging.

Example:
{
  "level": "INFO",
  "service": "tool-executor",
  "requestId": "request-123",
  "toolId": "finance.stock-pnl",
  "event": "execution.completed",
  "durationMs": 1250
}


Never log passwords, access tokens, API keys or complete sensitive documents.

Track:
Metric	Purpose
Request count	Usage
Error rate	Reliability
Latency	Performance
Login failures	Security
Tool execution time	Performance
Queue depth	Backlog
Failed jobs	Reliability
Storage usage	Capacity
Email delivery failures	Communications

Use OpenTelemetry for traces and standardized instrumentation.

Create:
/health
/health/ready
/health/live


Also implement:
- Error monitoring.
- Security alerts.
- Backup monitoring.
- Incident runbooks.
- Cost monitoring.

16. Testing strategy
Use a testing pyramid.
#chatgpt-mermaid-_r_2g9_{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:14px;fill:rgb(255, 255, 255);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_2g9_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_2g9_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_2g9_ .error-icon{fill:rgba(255, 255, 255, 0.03);}#chatgpt-mermaid-_r_2g9_ .error-text{fill:rgb(255, 255, 255);stroke:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_2g9_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_2g9_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_2g9_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_2g9_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_2g9_ .marker{fill:rgba(255, 255, 255, 0.498);stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2g9_ .marker.cross{stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2g9_ svg{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:14px;}#chatgpt-mermaid-_r_2g9_ p{margin:0;}#chatgpt-mermaid-_r_2g9_ .label{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ .cluster-label text{fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ .cluster-label span{color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_2g9_ .label text,#chatgpt-mermaid-_r_2g9_ span{fill:rgb(255, 255, 255);color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ .node rect,#chatgpt-mermaid-_r_2g9_ .node circle,#chatgpt-mermaid-_r_2g9_ .node ellipse,#chatgpt-mermaid-_r_2g9_ .node polygon,#chatgpt-mermaid-_r_2g9_ .node path{fill:rgb(26, 40, 61);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .rough-node .label text,#chatgpt-mermaid-_r_2g9_ .node .label text,#chatgpt-mermaid-_r_2g9_ .image-shape .label,#chatgpt-mermaid-_r_2g9_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_2g9_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .rough-node .label,#chatgpt-mermaid-_r_2g9_ .node .label,#chatgpt-mermaid-_r_2g9_ .image-shape .label,#chatgpt-mermaid-_r_2g9_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_2g9_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_2g9_ .root .anchor path{fill:rgba(255, 255, 255, 0.498)!important;stroke-width:0;stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2g9_ .arrowheadPath{fill:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2g9_ .edgePath .path{stroke:rgba(255, 255, 255, 0.498);stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .flowchart-link{stroke:rgba(255, 255, 255, 0.498);fill:none;}#chatgpt-mermaid-_r_2g9_ .edgeLabel{background-color:rgb(24, 24, 24);text-align:center;}#chatgpt-mermaid-_r_2g9_ .edgeLabel p{background-color:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2g9_ .edgeLabel rect{opacity:0.5;background-color:rgb(24, 24, 24);fill:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2g9_ .labelBkg{background-color:rgba(24, 24, 24, 0.5);}#chatgpt-mermaid-_r_2g9_ .cluster rect{fill:rgba(255, 255, 255, 0.03);stroke:rgba(255, 255, 255, 0.082);stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .cluster text{fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ .cluster span{color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:12px;background:rgba(255, 255, 255, 0.03);border:1px solid rgba(255, 255, 255, 0.082);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_2g9_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2g9_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_2g9_ .icon-shape,#chatgpt-mermaid-_r_2g9_ .image-shape{background-color:rgb(24, 24, 24);text-align:center;}#chatgpt-mermaid-_r_2g9_ .icon-shape p,#chatgpt-mermaid-_r_2g9_ .image-shape p{background-color:rgb(24, 24, 24);padding:2px;}#chatgpt-mermaid-_r_2g9_ .icon-shape .label rect,#chatgpt-mermaid-_r_2g9_ .image-shape .label rect{opacity:0.5;background-color:rgb(24, 24, 24);fill:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2g9_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_2g9_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_2g9_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_2g9_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_2g9_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_2g9_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_2g9_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_2g9_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2g9_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_2g9_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2g9_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_2g9_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_2g9_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_2g9_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_2g9_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .node rect,#chatgpt-mermaid-_r_2g9_ .node circle,#chatgpt-mermaid-_r_2g9_ .node ellipse,#chatgpt-mermaid-_r_2g9_ .node polygon,#chatgpt-mermaid-_r_2g9_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_2g9_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_2g9_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_2g9_ .edgePaths .flowchart-link{stroke:rgba(255, 255, 255, 0.498);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_2g9_ .marker{fill:rgba(255, 255, 255, 0.498);stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2g9_ :root{--mermaid-font-family:-apple-system,"system-ui","Segoe UI",sans-serif;}Unit TestsIntegration TestsContract TestsEnd-to-End TestsSecurity TestsRelease Confidence





Test category	Technology
Unit	Vitest
Component	Testing Library
E2E	Playwright
Accessibility	axe-core
API contracts	OpenAPI/schema tests
Security	OWASP ZAP and targeted tests
Load	k6
Database	PostgreSQL test environment

Critical E2E scenarios:
1. Visitor opens homepage.
2. Visitor browses public tools.
3. Visitor registers.
4. User verifies email.
5. User logs in.
6. User executes a public tool.
7. User attempts a private tool and is denied.
8. Admin grants access.
9. User executes the private tool.
10. Admin revokes access.
11. User loses access.
12. Password recovery works.
13. User logs out.
Target 90%+ test coverage for domain and authorization logic, with meaningful integration and contract coverage.

17. CI/CD and deployment
Git workflow
main
  |
  ├── feature/authentication
  ├── feature/tool-registry
  ├── feature/portfolio
  ├── feature/admin-dashboard
  └── fix/authorization


Use pull requests and short-lived branches.
CI pipeline
Every pull request must run:
1. Prettier.
2. ESLint.
3. TypeScript checks.
4. Unit tests.
5. Integration tests.
6. Architecture checks.
7. Dependency security scans.
8. Secret scanning.
9. Production build.
10. Preview deployment.
11. E2E tests.
12. Accessibility tests.
Environments
Environment	Purpose
Local	Development
Test	Automated testing
Staging	Release verification
Production	Real users

Keep separate secrets, credentials and storage for each environment.
Initial deployment cost
Service	Initial cost
Cloudflare hosting	₹0
Supabase Free	₹0
Resend Free	₹0
GitHub Free	₹0
Free subdomain	₹0
Local Ollama	₹0 additional
Custom domain	Deferred

Free-tier limits apply. Supabase Free projects can pause after inactivity and do not include automatic backups. Cloudflare Workers free requests have execution limits. Validate current provider terms before production release.
Backup strategy
- Encrypted database exports.
- Storage metadata backups.
- Migration history in Git.
- Recovery documentation.
- Restoration testing.
- Credential recovery process.
- Rollback procedures.
Initial recovery objectives: maximum 24-hour RPO and four-hour RTO, with better targets as the platform grows.

18. Implementation roadmap
Follow this sequence. Do not implement everything simultaneously.
Complete development roadmap
1. Phase 0 — Discovery
   - Inspect Portfolio directory.
   - Inventory existing projects.
   - Inspect agent skills.
   - Identify reusable components.
   - Identify dependencies.
   - Identify security risks.
   - Approve initial scope.
   Deliverable: Repository inventory and risk assessment.
2. Phase 1 — Foundation
   - Create monorepo.
   - Configure pnpm.
   - Configure TypeScript.
   - Create shared packages.
   - Establish dependency boundaries.
   - Configure CI/CD.
   - Create database migrations.
   - Deploy initial application.
   Deliverable: Working application and deployment.
3. Phase 2 — Design system and public website
   - Finalize visual direction.
   - Build design tokens.
   - Build components.
   - Build homepage.
   - Build About page.
   - Build portfolio.
   - Build tools directory.
   - Build contact form.
   - Implement accessibility and SEO.
   Deliverable: Complete responsive public website.
4. Phase 3 — Authentication and security
   - Supabase Auth.
   - Registration/login.
   - Email verification.
   - Password recovery.
   - User profiles.
   - Roles and permissions.
   - RLS.
   - MFA.
   - Audit logs.
   Deliverable: Secure multi-user foundation.
5. Phase 4 — Tool registry and administration
   - Tool manifest.
   - Tool categories.
   - Tool versions.
   - Search and filters.
   - Admin tool manager.
   - Visibility controls.
   - User permissions.
   - Publishing workflow.
   Deliverable: Dynamic tool marketplace.
6. Phase 5 — Execution engine
   - Execution router.
   - Runtime adapters.
   - API integration.
   - Worker integration.
   - Background queues.
   - Execution history.
   - Quotas and timeouts.
   Deliverable: Independent tool execution framework.
7. Phase 6 — Integrations
   - Email provider.
   - Storage provider.
   - AI gateway.
   - Ollama.
   - MCP gateway.
   - External APIs.
   - Local AI gateway.
   Deliverable: Integrated AI and developer ecosystem.
8. Phase 7 — Existing tools
   - Audit each existing tool.
   - Build adapters.
   - Add tests.
   - Register manifests.
   - Configure permissions.
   - Publish approved tools.
   Deliverable: Existing applications integrated.
9. Phase 8 — Operational readiness
   - Logging.
   - Monitoring.
   - Backup.
   - Restore tests.
   - Performance testing.
   - Security testing.
   - Documentation.
   Deliverable: Production-ready operational foundation.
10. Phase 9 — Release candidate
    - Full regression.
    - Accessibility audit.
    - Security review.
    - Mobile testing.
    - Recovery test.
    - Deployment verification.
    Deliverable: Approved release candidate.
11. Phase 10 — Production release
    - Publish website.
    - Enable registration.
    - Publish approved tools.
    - Configure monitoring.
    - Gather feedback.
    - Fix launch issues.
    Deliverable: Publicly available platform.


19. Agent-driven development policy
This platform should be understandable to Codex, Claude Code, Gemini CLI and other compatible agents.
Agent roles
Role	Responsibility
Architect	Architecture and design decisions
Product analyst	Requirements
UI/UX	Visual design and accessibility
Frontend	Next.js and UI
Backend	Business logic and APIs
Database	Schema and migrations
Security	Threat modelling and security
QA	Automated tests
DevOps	CI/CD and hosting
Reviewer	Independent review

Mandatory agent instructions
Create AGENTS.md in the root.
# Project Instructions

1. Read README.md and AGENTS.md.
2. Read relevant architecture documentation.
3. Inspect existing code before modifying anything.
4. Check Git status.
5. Never overwrite existing work without approval.

## Architecture
- Follow modular architecture.
- Respect dependency boundaries.
- Use provider interfaces.
- Keep domain logic framework-independent.
- Avoid unnecessary microservices.

## Security
- Deny by default.
- Verify permissions server-side.
- Validate all inputs.
- Never expose secrets.
- Protect user-owned resources.
- Never bypass RLS.

## UI
- Follow the central design system.
- Maintain responsiveness.
- Maintain accessibility.
- Implement loading and error states.

## Testing
- Add tests for new business logic.
- Add authorization regression tests.
- Run relevant tests.
- Never claim tests passed without execution.

## Database
- Use migrations.
- Never make undocumented schema changes.
- Do not perform destructive production operations.

## Documentation
- Update docs with implementation changes.
- Record major decisions in ADRs.
- Document environment variables.

## Completion report
- Changes made.
- Files modified.
- Tests executed.
- Results.
- Security implications.
- Known limitations.
- Follow-up tasks.


Superpowers workflow
If obra/superpowers is installed, use the relevant available skills:
Activity	Skill workflow
Feature exploration	Brainstorming
Implementation planning	Writing plans
Implementation	Executing plans
Bug fixing	Systematic debugging
Test-first development	Test-driven development
Final validation	Verification before completion
Code review	Requesting code review

Follow the exact installed skill instructions rather than assuming identical versions across agents.
Agent workflow
#chatgpt-mermaid-_r_2gp_{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:14px;fill:rgb(255, 255, 255);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_2gp_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_2gp_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_2gp_ .error-icon{fill:rgba(255, 255, 255, 0.03);}#chatgpt-mermaid-_r_2gp_ .error-text{fill:rgb(255, 255, 255);stroke:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_2gp_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_2gp_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_2gp_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_2gp_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_2gp_ .marker{fill:rgba(255, 255, 255, 0.498);stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2gp_ .marker.cross{stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2gp_ svg{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:14px;}#chatgpt-mermaid-_r_2gp_ p{margin:0;}#chatgpt-mermaid-_r_2gp_ .label{font-family:-apple-system,"system-ui","Segoe UI",sans-serif;color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ .cluster-label text{fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ .cluster-label span{color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_2gp_ .label text,#chatgpt-mermaid-_r_2gp_ span{fill:rgb(255, 255, 255);color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ .node rect,#chatgpt-mermaid-_r_2gp_ .node circle,#chatgpt-mermaid-_r_2gp_ .node ellipse,#chatgpt-mermaid-_r_2gp_ .node polygon,#chatgpt-mermaid-_r_2gp_ .node path{fill:rgb(26, 40, 61);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .rough-node .label text,#chatgpt-mermaid-_r_2gp_ .node .label text,#chatgpt-mermaid-_r_2gp_ .image-shape .label,#chatgpt-mermaid-_r_2gp_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_2gp_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .rough-node .label,#chatgpt-mermaid-_r_2gp_ .node .label,#chatgpt-mermaid-_r_2gp_ .image-shape .label,#chatgpt-mermaid-_r_2gp_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_2gp_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_2gp_ .root .anchor path{fill:rgba(255, 255, 255, 0.498)!important;stroke-width:0;stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2gp_ .arrowheadPath{fill:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2gp_ .edgePath .path{stroke:rgba(255, 255, 255, 0.498);stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .flowchart-link{stroke:rgba(255, 255, 255, 0.498);fill:none;}#chatgpt-mermaid-_r_2gp_ .edgeLabel{background-color:rgb(24, 24, 24);text-align:center;}#chatgpt-mermaid-_r_2gp_ .edgeLabel p{background-color:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2gp_ .edgeLabel rect{opacity:0.5;background-color:rgb(24, 24, 24);fill:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2gp_ .labelBkg{background-color:rgba(24, 24, 24, 0.5);}#chatgpt-mermaid-_r_2gp_ .cluster rect{fill:rgba(255, 255, 255, 0.03);stroke:rgba(255, 255, 255, 0.082);stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .cluster text{fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ .cluster span{color:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system,"system-ui","Segoe UI",sans-serif;font-size:12px;background:rgba(255, 255, 255, 0.03);border:1px solid rgba(255, 255, 255, 0.082);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_2gp_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(255, 255, 255);}#chatgpt-mermaid-_r_2gp_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_2gp_ .icon-shape,#chatgpt-mermaid-_r_2gp_ .image-shape{background-color:rgb(24, 24, 24);text-align:center;}#chatgpt-mermaid-_r_2gp_ .icon-shape p,#chatgpt-mermaid-_r_2gp_ .image-shape p{background-color:rgb(24, 24, 24);padding:2px;}#chatgpt-mermaid-_r_2gp_ .icon-shape .label rect,#chatgpt-mermaid-_r_2gp_ .image-shape .label rect{opacity:0.5;background-color:rgb(24, 24, 24);fill:rgb(24, 24, 24);}#chatgpt-mermaid-_r_2gp_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_2gp_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_2gp_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_2gp_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_2gp_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_2gp_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_2gp_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_2gp_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2gp_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_2gp_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_2gp_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_2gp_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_2gp_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_2gp_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_2gp_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .node rect,#chatgpt-mermaid-_r_2gp_ .node circle,#chatgpt-mermaid-_r_2gp_ .node ellipse,#chatgpt-mermaid-_r_2gp_ .node polygon,#chatgpt-mermaid-_r_2gp_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_2gp_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_2gp_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_2gp_ .edgePaths .flowchart-link{stroke:rgba(255, 255, 255, 0.498);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_2gp_ .marker{fill:rgba(255, 255, 255, 0.498);stroke:rgba(255, 255, 255, 0.498);}#chatgpt-mermaid-_r_2gp_ :root{--mermaid-font-family:-apple-system,"system-ui","Segoe UI",sans-serif;}Receive TaskRead InstructionsInspect Existing CodeUnderstand RequirementsCreate PlanReview ArchitectureImplement TestsImplement FeatureRun VerificationPassed?Fix IssuesIndependent ReviewUpdate DocumentationCompletion ReportNoYes





For parallel agents:
- Assign separate modules.
- Define interfaces before parallel work.
- Use separate branches.
- Avoid simultaneous migration changes.
- Review integration changes.
- Never let multiple agents independently change shared architecture without approval.

20. Documentation structure
Maintain all engineering documentation in the repository.
docs/
│
├── 00-MASTER-PLAN.md
│
├── product/
│   ├── requirements.md
│   ├── personas.md
│   └── user-journeys.md
│
├── architecture/
│   ├── system-architecture.md
│   ├── application-architecture.md
│   ├── module-boundaries.md
│   └── integration-architecture.md
│
├── design/
│   ├── visual-direction.md
│   ├── design-tokens.md
│   ├── components.md
│   └── accessibility.md
│
├── security/
│   ├── security-policy.md
│   ├── threat-model.md
│   ├── authentication.md
│   ├── authorization.md
│   └── privacy.md
│
├── database/
│   ├── schema.md
│   ├── relationships.md
│   └── backup-recovery.md
│
├── integrations/
│   ├── provider-contracts.md
│   ├── email.md
│   ├── ai.md
│   ├── mcp.md
│   └── local-ai.md
│
├── testing/
│   ├── testing-strategy.md
│   └── security-testing.md
│
├── operations/
│   ├── monitoring.md
│   ├── logging.md
│   └── incident-response.md
│
├── deployment/
│   ├── environments.md
│   ├── ci-cd.md
│   └── release.md
│
├── roadmap/
│   ├── milestones.md
│   ├── backlog.md
│   └── progress.md
│
└── decisions/
    ├── ADR-001-modular-architecture.md
    ├── ADR-002-database.md
    ├── ADR-003-authentication.md
    ├── ADR-004-tool-execution.md
    ├── ADR-005-hosting.md
    └── ADR-006-provider-abstraction.md


ADR format
Every major architecture decision should record:
# ADR-XXX: Decision title

## Status

Proposed / Accepted / Superseded

## Context

Why is this decision needed?

## Decision

What is being selected?

## Alternatives

What else was considered?

## Consequences

Benefits and limitations.

## Migration Strategy

How can this be replaced?

## Security Implications

What risks does it introduce?



21. Acceptance criteria
The platform is not ready for release until these requirements are satisfied.
Public website
- [ ] Homepage works.
- [ ] Portfolio is dynamic.
- [ ] Tools directory is searchable.
- [ ] Public tools work without login.
- [ ] Private tools are protected.
- [ ] Mobile layouts work.
- [ ] SEO is configured.
- [ ] Accessibility checks pass.
Authentication
- [ ] Registration works.
- [ ] Email verification works.
- [ ] Login/logout works.
- [ ] Password recovery works.
- [ ] Admin MFA works.
- [ ] Privilege escalation is prevented.
- [ ] Cross-user access is prevented.
Tool ecosystem
- [ ] Tools can be registered dynamically.
- [ ] Manifests are validated.
- [ ] Tools can be versioned.
- [ ] Permissions can be granted and revoked.
- [ ] Execution status is visible.
- [ ] Multiple execution modes work.
- [ ] Adapter contract tests pass.
Infrastructure
- [ ] Migrations are reproducible.
- [ ] Backups work.
- [ ] Restore is tested.
- [ ] Email works.
- [ ] CI/CD works.
- [ ] Staging works.
- [ ] Production deployment works.
- [ ] Monitoring is available.
Agent readiness
- [ ] AGENTS.md exists.
- [ ] Architecture documents exist.
- [ ] ADRs are maintained.
- [ ] Agent workflow is documented.
- [ ] Progress tracking exists.
- [ ] Independent reviews are possible.

22. Future evolution
Prepare for these features, but do not build them in the initial release.
Feature	Future capability
Subscriptions	Free, Pro, Enterprise
Billing	Payment gateway adapter
API marketplace	Developer API keys
Teams	Organizations and memberships
External developers	Tool publishing
Marketplace	Tool submissions and approval
Agent ecosystem	Agent runtime
Advanced analytics	Usage analytics
Mobile application	Shared API and identity
SDK	External tool integrations

Future entitlement structure:
Plans
  |
  ├── Free
  ├── Pro
  └── Enterprise

Entitlements
  |
  ├── Tool access
  ├── Execution limits
  ├── Storage limits
  ├── AI usage
  └── API access



23. Initial tool catalogue
Based on your existing projects, I recommend starting with these categories.
Category	Candidate tools
Finance	Form 16 Parser, 26AS Parser, Stock P&L Analyzer
Productivity	PDF Analyzer, Document Extractor
AI	AI Story Generator, Content Assistant
Developer	MCP Playground, API Utilities
Automation	Workflow Automation, Data Processing

For each portfolio project, publish:
- Problem statement.
- Solution.
- Architecture.
- Technology stack.
- Engineering decisions.
- Challenges.
- Performance improvements.
- Business impact.
- Screenshots.
- Demo URL.
- GitHub URL, if public.
Only publish professional work that you are authorized to disclose.

24. Initial architecture decision register
These are proposed decisions, subject to validation during discovery.
ID	Decision
ADR-001	Modular monolith initially
ADR-002	PostgreSQL as primary database
ADR-003	Supabase Auth initially
ADR-004	Next.js + TypeScript
ADR-005	Cloudflare hosting initially
ADR-006	Ports and adapters
ADR-007	Dynamic tool registry
ADR-008	Independent tool runtimes
ADR-009	REST + OpenAPI
ADR-010	Central design system
ADR-011	RBAC + resource-level permissions
ADR-012	Independent MCP integration layer
ADR-013	Resend email provider
ADR-014	GitHub CI/CD
ADR-015	Automated backup and recovery


25. First development backlog
This is the exact order I would start implementing.
Task	Priority
Inspect existing Portfolio directory	P0
Inventory existing projects	P0
Inspect available agent skills	P0
Inventory reusable components	P0
Approve architecture	P0
Establish AGENTS.md	P0
Create ADRs	P0
Initialize monorepo	P0
Configure CI/CD	P0
Build design system	P0
Create database schema	P0
Implement authentication	P0
Implement authorization	P0
Build public website	P0
Build tool registry	P0
Build admin dashboard	P1
Build execution router	P0
Integrate first sample tool	P0
Integrate email	P1
Integrate existing tools	P1
Integrate MCP	P2
Integrate Ollama	P2
Complete security testing	P0
Production release	P0


26. Final execution strategy
The complete journey
1. Discover existing projects and agent resources.
2. Finalize requirements and architecture.
3. Establish engineering policies and repository structure.
4. Build the design system and public experience.
5. Implement authentication, authorization and security.
6. Build the tool registry and admin dashboard.
7. Build independent execution infrastructure.
8. Integrate existing projects, AI and MCP.
9. Validate reliability, security and performance.
10. Deploy and release the platform.

My final recommendations
Five principles should never be compromised:
1. Security first: Every private tool must enforce access independently.
2. Provider independence: External infrastructure must be replaceable through adapters.
3. Tool independence: Tools should not depend on the website's internal implementation.
4. Design consistency: Every application should feel like part of the same product.
5. Agent governance: Agents must follow documented architecture, testing and review policies.
The final outcome should allow you to develop your 10th or 50th tool independently, register it, assign permissions and publish it without rebuilding the central platform.

The first action should be Phase 0: inspect and inventory everything already present in /Users/admin/Downloads/Portfolio. Do not start by rewriting existing projects or generating the entire application in one shot.

This blueprint defines the target architecture and release process. Actual provider compatibility, existing-project reuse and security decisions must be verified during discovery before implementation begins.


Finalize the architecture and implementation plan for my personal technology platform. Access: Both public registration and private access controlled by me. Tool scope: Both existing projects and new tools. Execution: All of the above. Email: Professional email + website notifications. Domain: Start free, purchase a domain later. Provide the production-oriented architecture, technology choices, database schema, security model, deployment plan and implementation phases, optimizing initial cost to zero.
Personal Technology Platform — Production Architecture & Implementation Plan
Architecture finalized Zero-cost-first

The recommended solution is a modular, multi-tool developer platform with centralized authentication, permissions, tool discovery, execution management and administration.

It should support three different identities:

You: Platform owner and administrator.

Registered users: Can access public tools and any private tools you authorize.

Visitors: Can browse your portfolio and use tools explicitly marked public.

It should also support independently developed applications, cloud APIs, local AI models and MCP servers without tying everything to the website's frontend.

My recommendation is to build a modular monolith first, with independent execution services where necessary. This avoids the operational complexity of microservices while keeping the architecture extensible.

1. Final technology choices
Core platform stack
Making a custom 404 page in Next.js - DEV Community
Next.js + TypeScript

Frontend, server components, API layer, admin dashboard

Primary application

Why Cloudflare’s Outage Should Terrify AI-First Startups | by Abhinav | Medium
Cloudflare Workers

Application hosting, lightweight APIs, routing, scheduled tasks

Supabase - Review, Pricing & Alternatives | Delv
Supabase + PostgreSQL

Database, authentication, authorization, file storage

Resend Logo Vector File Download | Logowik
Resend

Transactional emails and notifications

Oakstone & Github | Executive Search for GTM SaaS
GitHub

Source control, CI/CD, project management

Logo Tailwind CSS – Logos PNG
Tailwind CSS + shadcn/ui

Consistent, responsive user interface

Additional technologies:

Requirement

Technology

Forms and validation

React Hook Form + Zod

Database access

Supabase client + SQL migrations

Background jobs

Cloudflare Queues, where suitable

Caching

Cloudflare Cache / application cache

File processing

Isolated processing services

Logging

Structured JSON logs

Error tracking

Sentry free tier or equivalent

API documentation

OpenAPI

Testing

Vitest + Playwright

Package management

pnpm

Why not Java Spring Boot for the central platform?

You already have Java/Spring Boot experience, but a separate Spring Boot deployment would introduce additional hosting and operational requirements. Next.js and Workers are a more economical starting point.

However, existing Java applications can remain independent services and integrate through APIs.

2. High-level system architecture
This is the architecture I would implement.

Visitors and Registered Users
Cloudflare Edge
Next.js Application
Supabase Auth
Tool Registry API
Portfolio and Content
PostgreSQL
Authorization and RLS
Tool Execution Router
Cloudflare Tool Workers
External REST APIs
Background Jobs
MCP Services
Resend Email Service
User Email Inbox
Local AI / Ollama
Component responsibilities
Component

Responsibility

Cloudflare

Public entry point, hosting and edge protection

Next.js

All user-facing pages and application APIs

Supabase Auth

Signup, login, sessions, password reset

PostgreSQL

Users, tools, permissions, projects, activity

Tool Registry

Discover and describe available tools

Execution Router

Decide how and where a tool runs

Cloudflare Workers

Lightweight tool execution

External APIs

Independent applications and services

Background Jobs

Long-running or asynchronous work

MCP Services

Connect developer tools and AI agents

Ollama

Optional connection to local AI models

Resend

Application-generated emails

One important hosting detail: Cloudflare's current Next.js guidance recommends its newer vinext deployment path for new projects, while OpenNext remains a documented alternative for compatibility. I would begin with the Cloudflare-supported scaffold and validate the required Next.js features before locking the deployment adapter. 

Cloudflare Workers docs
+2

3. Application architecture and repository structure
Use a monorepo. It allows you to develop multiple tools independently while reusing authentication, UI components, database access and common functionality.

Recommended structure:

personal-platform/
│
├── apps/
│   ├── web/
│   │   ├── app/
│   │   │   ├── (public)/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── portfolio/
│   │   │   │   ├── tools/
│   │   │   │   └── about/
│   │   │   │
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   └── register/
│   │   │   │
│   │   │   ├── workspace/
│   │   │   ├── admin/
│   │   │   └── api/
│   │   └── components/
│   │
│   └── workers/
│       ├── tool-executor/
│       ├── background-jobs/
│       └── notifications/
│
├── packages/
│   ├── ui/
│   ├── database/
│   ├── auth/
│   ├── permissions/
│   ├── tool-sdk/
│   ├── tool-registry/
│   ├── email/
│   ├── validation/
│   └── types/
│
├── tools/
│   ├── form16-parser/
│   ├── tax26as-parser/
│   ├── stock-pnl-parser/
│   ├── pdf-analyzer/
│   └── ai-story-generator/
│
├── supabase/
│   ├── migrations/
│   ├── seed.sql
│   └── config.toml
│
├── tests/
│   ├── integration/
│   ├── e2e/
│   └── security/
│
├── docs/
│   ├── architecture/
│   ├── api/
│   └── tool-development/
│
├── pnpm-workspace.yaml
└── package.json
The listed tools are initial integration candidates, not assumptions that every one must be rebuilt. Existing applications should be wrapped with adapters wherever possible.

Tool integration contract
Every tool should follow a standard interface.

For example:

interface PlatformTool {
  id: string;
  name: string;
  description: string;
  version: string;

  visibility:
    | "public"
    | "authenticated"
    | "restricted"
    | "private";

  executionType:
    | "embedded"
    | "edge"
    | "api"
    | "job"
    | "mcp";

  inputSchema: unknown;
  outputSchema: unknown;

  execute(
    input: unknown,
    context: ToolContext
  ): Promise<ToolResult>;
}

The platform will not need to know the internal implementation of each tool. It only needs to know how to authenticate the user, validate the request, authorize access and route execution.

For example:

A PDF parser can run through an independent API.

A calculator can execute directly in a Worker.

A video generator can submit a background job.

An MCP integration can connect to an MCP server.

An AI tool can call an external LLM or local Ollama service.

Do not execute arbitrary uploaded JavaScript or Python directly inside the main application. Register trusted, versioned tool deployments instead.

4. Database design
Use PostgreSQL as the single source of truth.

I recommend the following entities.

Core tables
Table

Important fields

Purpose

profiles

id, display_name, avatar_url

User profiles

user_roles

user_id, role

Owner, admin, user

projects

id, title, slug, description, status

Portfolio projects

project_technologies

project_id, technology

Technology tags

tools

id, slug, name, description, visibility

Tool directory

tool_versions

tool_id, version, deployment_ref

Tool releases

tool_categories

id, name, slug

Tool categories

tool_permissions

tool_id, user_id, permission

Individual access

tool_runs

id, tool_id, user_id, status

Execution history

tool_favorites

user_id, tool_id

User favorites

audit_logs

actor_id, action, metadata

Security audit

notifications

user_id, title, read_at

In-app notifications

contact_messages

sender, email, message

Contact form

Relationships
PROFILES
USER_ROLES
TOOL_PERMISSIONS
TOOLS
TOOL_VERSIONS
TOOL_CATEGORIES
TOOL_RUNS
PROJECTS
PROJECT_TECHNOLOGIES
NOTIFICATIONS
AUDIT_LOGS
has
receives
grants
contains
belongs
executes
initiates
uses
receives
performs
Important database decisions
A. Tool visibility

Store a visibility value on every tool:

Value

Access

public

Anyone

authenticated

Any registered user

restricted

Explicitly authorized users

private

Owner and specifically authorized administrators

B. Separate roles from tool permissions

A user's platform role should not automatically determine every tool permission.

For example, a normal registered user may have access to one restricted tool without becoming an administrator.

C. Version tools

A tool should have a version history. This lets you update a tool without losing the ability to roll back to a previous working release.

D. Keep execution history lightweight

Record execution time, status, tool version and error category. Avoid storing sensitive financial documents, raw passwords or complete user inputs in logs.

Database migration strategy
Use version-controlled SQL migrations.

001_initial_schema.sql
002_user_roles.sql
003_projects.sql
004_tool_registry.sql
005_tool_permissions.sql
006_tool_execution.sql
007_audit_logs.sql
008_notifications.sql
009_rls_policies.sql
This ensures the database can be reconstructed consistently.

5. Authentication and security architecture
This is a critical part because you want public registration and private tools on the same platform.

User roles
Owner

Full control
Manage users and roles.

Add, edit, publish and disable tools.

Grant and revoke access.

Manage projects and platform settings.

View audit and execution records.

Administrator

Operational control
Manage approved users and content.

Manage assigned tools.

Monitor execution and errors.

Cannot change owner privileges.

Registered user

Standard
Access public tools.

Access authenticated tools.

Use tools explicitly granted to them.

Manage their own profile and preferences.

Visitor

Anonymous
View portfolio and projects.

Explore public tools.

Use public tools within usage limits.

Register for an account.

Login and registration flow
Open Website
Logged In?
Browse Public Content
Register or Login
Supabase Authentication
Default User Role
Load User Profile
Open Tool
Permission Check
Execute Tool
Access Denied
Record Execution
No
Yes
Allowed
Denied
Security requirements
I would enforce the following from the beginning:

Security control

Implementation

Password security

Supabase Auth

Session management

Secure, HTTP-only cookies

Email verification

Required for registered users

Admin MFA

Mandatory

Authorization

Server-side role and permission checks

Database access

PostgreSQL Row Level Security

API protection

Authentication + authorization

Rate limiting

Cloudflare

Bot protection

Cloudflare Turnstile

Secrets

Cloudflare environment secrets

File uploads

Type, size and content validation

Audit trail

Dedicated audit logs

HTTPS

Cloudflare

Data retention

Configurable per tool

Important implementation rules:

New registrations always receive the standard user role.

Users cannot assign themselves roles.

The first owner account must be provisioned manually through a secure administrative process.

Every private API must independently verify authorization.

Never rely on a hidden button or frontend route as a security boundary.

Enable RLS on every user-facing database table.

Never expose Supabase service-role keys or third-party API secrets to the browser.

Restrict tool execution time, request size and concurrent usage.

Validate external URLs and block private-network destinations to prevent SSRF.

For sensitive document processing, minimize retention and delete temporary files after processing.

Special consideration for your financial tools
Your Form 16, 26AS and Stock P&L parsers can potentially handle sensitive financial documents.

I recommend:

Process files in isolated services.

Do not retain uploaded documents by default.

Avoid storing extracted PAN, bank details or financial information in application logs.

Provide explicit deletion controls.

Use short-lived download links.

Encrypt any data that genuinely needs to be retained.

6. Tool execution architecture
This is where the platform becomes significantly more powerful than a normal portfolio.

I recommend five execution modes.

Mode

Example

Execution

Embedded

Calculator

Frontend

Edge

Lightweight parser

Cloudflare Worker

API

Existing Java application

External API

Job

Video generation

Background worker

MCP

Developer automation

MCP service

Execution lifecycle
Database
Tool Service
Tool Router
Auth and Access
Website
User
Database
Tool Service
Tool Router
Auth and Access
Website
User
Submit tool request
Validate identity and permission
Check access rules
Permission result
Authorized
Execute tool
Route request
Tool result
Record execution status
Return result
Display result
Long-running tools
Do not hold a browser request open while a large task executes.

For video generation, complex AI processing or large PDF workloads:

User submits a task.

Backend creates a job.

Queue receives the job.

Worker processes it.

Job status is updated.

User sees progress.

Completion notification is sent.

Suggested job states:

PENDING
  |
QUEUED
  |
RUNNING
  |
  +----> COMPLETED
  |
  +----> FAILED
  |
  +----> CANCELLED
Use Cloudflare Queues for compatible asynchronous work. Heavy CPU/GPU processing should run on a separate compute service or your local machine.

Local AI and MCP connectivity
You can integrate your existing Ollama models without making the local machine the primary hosting environment.

Website User
Cloud Platform
Secure Gateway
Tailscale or Secure Tunnel
Local AI Gateway
Ollama
MCP Servers
For this integration:

Keep Ollama and MCP services private.

Do not expose Ollama directly to the public internet.

Authenticate requests through a gateway.

Allowlist permitted tools and operations.

Set execution timeouts and concurrency limits.

Ensure the local machine is awake and connected.

When the machine is offline, the website should report that the local service is unavailable rather than silently failing.

7. Email architecture
Your email requirement has two separate parts.

Professional identity

hello@yourdomain.com

Incoming messages can be forwarded to your existing Gmail inbox using Cloudflare Email Routing.

Website-generated email

Registration confirmation

Password reset

Login verification

Contact form notifications

Tool completion notifications

Administrative alerts

These will use Resend.

Important: Zero-cost domain limitation
Because you want to start without purchasing a domain, there is one unavoidable limitation.

You cannot initially have a permanent branded address such as hello@yourdomain.com without owning the domain.

My proposed rollout:

Stage

Email setup

Initial

Existing Gmail address for contact

Initial

Supabase authentication email

Initial

Resend test setup

After domain purchase

hello@yourdomain.com

After domain purchase

Configure SPF, DKIM and DMARC

After domain purchase

Enable branded transactional emails

Optional

Forward incoming mail to Gmail

Cloudflare Email Routing is a forwarding service, not a conventional full mailbox. 

Cloudflare Email Service docs
+1

Resend's published free tier currently includes 3,000 emails monthly and 100 emails daily. 

Resend

For a production authentication system, configure a verified sending domain and test password recovery, verification and delivery before opening registration widely.

8. Hosting and deployment plan
Initial hosting
Service

Deployment

Initial cost

Website

Cloudflare Workers

₹0

Static assets

Cloudflare

₹0 within limits

Database

Supabase Free

₹0

Authentication

Supabase Free

₹0

Email

Resend Free

₹0 within quotas

Source control

GitHub Free

₹0

Local AI

Existing machine

₹0 additional hosting

Domain

workers.dev

₹0

Cloudflare currently documents 100,000 Workers requests per day on the free plan, with a 10 ms CPU-time limit per invocation. This makes it suitable for lightweight application work, not arbitrary heavy processing. 

Cloudflare Workers docs
+1

Supabase currently provides 500 MB database storage, 1 GB file storage and 50,000 monthly active users on its free tier. Its free projects can pause after one week of inactivity and do not include automatic backups. 

Supabase
+1

These constraints mean the architecture can start at ₹0, but should not be represented as a guaranteed production SLA.

Deployment environments
I recommend three environments:

Development

Local
Local Next.js development.

Local Supabase through Supabase CLI.

Mock email service.

Local test tools and Ollama.

Staging

Preview
Cloudflare preview deployment.

Test database or isolated test schema.

Synthetic user accounts and data.

End-to-end testing.

Production

Live
Cloudflare Workers.

Supabase production database.

Production email service.

Real user authentication and permissions.

Since Supabase Free has a two-active-project limit, I would initially use local Supabase for development and one hosted production project. Use a separate staging database/schema or another isolated environment only when needed. Do not mix test user data with real production users.

CI/CD pipeline
Developer Push
GitHub
Lint and Type Check
Unit Tests
Security Checks
Build
Preview Deployment
E2E Tests
Approved?
Fix Issues
Production Deployment
Smoke Tests
No
Yes
Deployment rules:

Every pull request creates a preview.

Main branch deploys to production only after checks pass.

Database migrations are reviewed and applied in a controlled order.

Keep rollback-capable tool versions.

Never run destructive migrations without a backup.

Use separate environment secrets.

9. Admin dashboard — what you should be able to control
You should not need to modify source code every time you add a tool, publish a project or grant access.

I recommend building these admin modules.

Platform administration
Overview

Users, tools, usage and platform health

Tool manager

Register, publish, disable and version tools

User manager

Users, roles, invitations and permissions

Portfolio manager

Projects, descriptions, images and links

Execution monitor

Job status, failures and execution metrics

Settings

Email, integrations, security and configuration

Example: Adding a new tool
Suppose you develop a new AI resume analyzer.

The workflow should be:

Open Admin → Tool Manager.

Select Add Tool.

Enter name, description and category.

Select execution type: API, Edge, Job or MCP.

Provide its registered deployment reference.

Select visibility.

Configure permissions and usage limits.

Test the integration.

Publish.

The public tools directory should automatically display the new tool if its visibility is public.

This is the most important feature for long-term maintainability.

10. Implementation phases
I would divide development into seven phases.

Development roadmap
Phase 1 — Platform foundation

Highest priority
Initialize monorepo.

Configure Next.js and TypeScript.

Set up Cloudflare deployment.

Configure Supabase and PostgreSQL.

Create database migrations.

Configure development and production environments.

Deliverable: Working deployed website with database connectivity.

Phase 2 — Authentication and authorization

Registration and login.

Email verification.

Password recovery.

User profiles.

Owner/admin/user roles.

RLS policies.

Private route and API protection.

Deliverable: Secure multi-user platform.

Phase 3 — Portfolio and public portal

Homepage.

About page.

Professional experience.

Project portfolio.

Technology showcase.

Contact form.

SEO and responsive design.

Deliverable: Public-facing technology portfolio.

Phase 4 — Tool registry and administration

Dynamic tool directory.

Categories and search.

Tool metadata.

Tool versioning.

Visibility settings.

User permissions.

Admin dashboard.

Deliverable: Tools can be registered and managed centrally.

Phase 5 — Tool integrations

Integrate existing parsers.

Create standard tool SDK.

Connect REST APIs.

Implement execution router.

Add background processing.

Add MCP connectivity.

Connect local AI gateway.

Deliverable: Multiple independently implemented tools working under one platform.

Phase 6 — Email, monitoring and security

Resend integration.

Notifications.

Cloudflare rate limits.

Audit logs.

Error monitoring.

Security testing.

Backup and recovery procedures.

Deliverable: Operationally maintainable platform.

Phase 7 — Production readiness

Performance testing.

Accessibility testing.

End-to-end testing.

Deployment automation.

Documentation.

Domain migration when purchased.

Deliverable: Publicly launchable platform.

Suggested priorities
Do not develop all the tools immediately.

The first release should include:

Feature

Priority

Homepage and portfolio

P0

Authentication

P0

Public/private permissions

P0

Dynamic tool registry

P0

Admin dashboard

P0

One or two working tools

P0

Email notifications

P1

Execution monitoring

P1

MCP integration

P1

Local AI integration

P2

Advanced analytics

P2

Subscription/payment system

Future

11. Expected operating costs and limitations
Target: ₹0 initial monthly cost
Component

Initial monthly cost

When you might pay

Cloudflare Workers

₹0

Higher usage or compute needs

Supabase

₹0

More storage, backups, reliability

Resend

₹0

Higher email volume

GitHub

₹0

Advanced team features

Cloudflare Email Routing

₹0

Requires a domain

Professional mailbox

Not available without domain

Domain and mailbox purchase

Ollama

₹0 additional

Hardware/electricity costs

Custom domain

₹0 initially

When you purchase it

Three limitations need to be understood:

Free hosting is not unlimited. Heavy PDF processing, AI inference and video generation should not run inside lightweight Workers.

Free database hosting is not a production backup strategy. Implement scheduled encrypted database exports and test restoration before onboarding users.

Public tools introduce abuse and resource costs. Use per-user quotas, anonymous rate limits, execution timeouts and file-size restrictions.

Supabase Free is suitable for initial development and a low-traffic launch, but its inactivity pausing and lack of automatic backups make it unsuitable as the only reliability mechanism for a business-critical service. 

Supabase
+1

12. Final architecture decisions
These are the decisions I would freeze for version 1.

Area

Final decision

Architecture

Modular monolith + independent tool services

Frontend

Next.js + TypeScript

Hosting

Cloudflare Workers

Database

Supabase PostgreSQL

Authentication

Supabase Auth

Authorization

RBAC + individual tool permissions + RLS

Tool management

Dynamic Tool Registry

UI

Tailwind CSS + shadcn/ui

Email

Resend

Source control

GitHub

Background execution

Cloudflare Queues

AI integration

External APIs + Ollama

MCP integration

Independent MCP services

Storage

Supabase Storage initially

Deployment

Automated CI/CD

Domain

Free subdomain initially

Useful official resources:

Cloudflare Workers documentation

Supabase documentation

Next.js documentation

Resend documentation

shadcn/ui components

13. What I would use as your initial tool catalogue
Based on the projects and technologies you've previously worked with, these are good candidates to organize into the platform:

Category

Initial projects

Finance

Form 16 Parser, 26AS Parser, Stock P&L Parser

AI

AI Story Generator, AI Content Assistant

Developer

MCP Playground, API Utilities

Productivity

PDF Analyzer, Document Extractor

Automation

Workflow Automation, Data Processing

For your professional portfolio, you can also showcase your distributed systems work, Java/Spring Boot projects, AI engineering experiments and sanitized descriptions of your MCP work. Do not expose proprietary Oracle code, internal telemetry, logs or confidential project details.

14. Recommended next step: Build the foundation
I would not start by implementing individual tools. First, create the platform foundation and ensure the authentication, registry, permissions and deployment work together.

The first deliverable should be:

A deployed website with:

Public homepage and portfolio.

Registration and login.

User dashboard.

Admin dashboard.

Dynamic tools directory.

Public/private tool permissions.

One working sample tool.

PostgreSQL database and migrations.

Automated deployment.

After this foundation, integrating your other tools becomes much easier.

One additional recommendation: keep the tool registry independent of the frontend. Eventually, you could expose a public API that allows other applications to discover your tools and their capabilities.

This makes the platform an actual tool ecosystem rather than just a collection of web pages.

I would use this architecture as the baseline for implementation, with zero paid infrastructure initially and no premature microservices.

can you share me where i can clone google EGM for /Users/admin/Downloads/Portfolio my portfolio at this path so that any agent can use that, also obra/superpowers, better can you give me copy paste terminal command
Worked for 5s
For your Mac, I recommend keeping both repositories inside your Portfolio directory so different coding agents can reference the same local copies.

I found the official repository for obra/superpowers:

obra/superpowers — GitHub

Google EGM: I couldn't identify a repository with that exact name. Did you mean Google Gemini CLI or Google ADK (Agent Development Kit)?

1. Clone Superpowers
Copy and paste this into Terminal:

mkdir -p /Users/admin/Downloads/Portfolio/agent-resources

cd /Users/admin/Downloads/Portfolio/agent-resources

git clone https://github.com/obra/superpowers.git

2. Recommended folder structure
/Users/admin/Downloads/Portfolio/
│
├── agent-resources/
│   └── superpowers/
│
├── projects/
├── tools/
├── experiments/
└── docs/
3. Make Superpowers available to agents
Cloning alone does not activate Superpowers in every agent. It needs to be installed using the appropriate integration for each agent.

For Codex CLI, the official repository documents installation through its plugin marketplace:

/plugins
Search for superpowers and install it. 

GitHub

For other agents, use their respective plugin integrations.

4. Verify the clone
cd /Users/admin/Downloads/Portfolio/agent-resources/superpowers

git status
ls skills

One clarification: When you say Google EGM, do you mean Google Gemini CLI, Google ADK, or another Google agent framework? I can then give you the exact official clone command and add it to the same directory.

i have added agents you can use those skills can you create a proper plan end to end and add that in Downloads/Portfolio folder, with every detail added, in the plan, what piece goes where, why, how, we want to create a policy where we create beautiful one and secured properly, and want to integrate all piece and it should be like any piece can be replaced with other one and it should work seemless, proper patterns and solid architecture should be used. i need end to end detailed plan from design to actual release
Worked for 2s
I would structure this as a proper engineering blueprint, not just a list of technologies or development tasks.

The plan should become the source of truth for every agent working inside /Users/admin/Downloads/Portfolio.

I would create the following documentation structure:

Portfolio/
│
├── agent-resources/
│   └── superpowers/
│
├── docs/
│   ├── 00-MASTER-PLAN.md
│   ├── 01-PRODUCT-REQUIREMENTS.md
│   ├── 02-SYSTEM-ARCHITECTURE.md
│   ├── 03-UI-UX-DESIGN-SYSTEM.md
│   ├── 04-SECURITY-POLICY.md
│   ├── 05-DATABASE-DESIGN.md
│   ├── 06-AUTHENTICATION-AUTHORIZATION.md
│   ├── 07-TOOL-PLUGIN-ARCHITECTURE.md
│   ├── 08-INTEGRATION-STRATEGY.md
│   ├── 09-API-CONTRACTS.md
│   ├── 10-TESTING-STRATEGY.md
│   ├── 11-DEVOPS-CICD.md
│   ├── 12-DEPLOYMENT-RELEASE.md
│   ├── 13-OBSERVABILITY-OPERATIONS.md
│   ├── 14-IMPLEMENTATION-ROADMAP.md
│   ├── 15-ACCEPTANCE-CRITERIA.md
│   └── decisions/
│       └── ADR-001-ARCHITECTURE.md
│
└── README.md
Engineering principles I would enforce
Replaceable components: Database, email provider, AI provider, authentication provider, hosting and tool execution must communicate through interfaces and adapters.

Security by design: Zero-trust authorization, least privilege, RLS, secrets management, secure sessions and threat modelling.

Beautiful UX: A consistent design system, responsive layouts, accessibility, polished interactions and excellent loading/error states.

Contract-driven development: Every integration must have defined inputs, outputs, error contracts and versioning.

Test-first implementation: Unit, integration, contract, security and end-to-end testing.

Agent-independent documentation: Any compatible coding agent should be able to understand the architecture, current progress, constraints and implementation instructions.

No premature complexity: Modular architecture first, independent services only where justified.

Release discipline: No feature reaches production without passing its security, testing and acceptance gates.

One limitation
I cannot directly inspect or write to your Mac's /Users/admin/Downloads/Portfolio folder from this chat. The local Work handoff was declined, so I haven't created any files or modified your directory.

To have the complete documentation created directly in that folder, open this conversation in Work mode and authorize local file access. The task can then inspect your existing agent resources and produce all the documents in the structure above, without implementing the application itself.

ok can you share all the data here itself, end to end every plan
share again, the data not visible
Personal Technology Platform — Complete Engineering Blueprint
Project location: /Users/admin/Downloads/Portfolio

Objective: Build a beautiful, secure, dynamic and extensible platform that combines your professional portfolio, public tools, private applications, AI capabilities, MCP integrations and developer utilities.

The platform must support multiple coding agents and allow infrastructure providers, tools and integrations to be replaced without rewriting the entire application.

This is the complete implementation blueprint, from initial discovery through production release.

1. Product vision
Build one central platform with four major areas.

Personal Technology Platform

One identity · Multiple applications · Centralized management

Portfolio

Experience, projects, achievements and technical articles.

Tools directory

Public and private applications with searchable capabilities.

Private workspace

Login, permissions, personal utilities and restricted tools.

AI & Developer platform

LLMs, MCP, APIs, automation and local models.

User types
User

Capabilities

Visitor

Browse portfolio and public tools

Registered user

Use authenticated tools

Invited user

Use specifically authorized private tools

Administrator

Manage users, tools and projects

Owner

Full platform administration

Core functionality
Public website
Homepage.

About/profile.

Professional experience.

Project portfolio.

Tools directory.

Individual tool pages.

Public tool execution.

Contact form.

Engineering blog.

SEO.

Authentication
Registration.

Login/logout.

Email verification.

Password recovery.

Secure sessions.

MFA for administrators.

User suspension.

Account deletion.

Private workspace
User dashboard.

Available tools.

Favorites.

Execution history.

Notifications.

Profile settings.

Tool management
Add and publish tools.

Change visibility.

Manage tool versions.

Grant/revoke permissions.

Configure execution.

Monitor tool health.

Track usage.

Administration
User management.

Role management.

Tool management.

Portfolio management.

Integration management.

Audit logs.

Monitoring.

Platform configuration.

2. Engineering constitution — mandatory policies
Every developer and coding agent must follow these rules.

Architecture policies
Use modular architecture.

Keep business logic independent of infrastructure.

Use interfaces for external providers.

Avoid circular dependencies.

Do not introduce microservices without justification.

Define contracts before implementing integrations.

Use independent execution environments for tools that need them.

Keep all major architectural decisions documented.

Replaceability policy
Every external dependency must have an adapter.

Capability

Initial provider

Possible replacement

Database

PostgreSQL / Supabase

Another PostgreSQL host

Authentication

Supabase Auth

OIDC provider

Email

Resend

SES, Postmark, SMTP

Storage

Supabase Storage

S3, R2, MinIO

Queue

Cloudflare Queues

SQS, RabbitMQ

AI

Ollama / API providers

Other compatible LLMs

Hosting

Cloudflare

Other compatible runtime

Logging

OpenTelemetry

Other telemetry backend

Tool execution

Runtime adapters

Worker, API, container

Important: Replaceability requires explicit contracts and migration plans. A database or identity provider cannot always be swapped with a simple configuration change.

Code quality policies
Area

Standard

Language

TypeScript strict

Formatting

Prettier

Linting

ESLint

Validation

Zod

Unit testing

Vitest

E2E testing

Playwright

API documentation

OpenAPI

Database changes

Version-controlled migrations

Package manager

pnpm

Git workflow

Feature branches and pull requests

Mandatory rules
No secrets in Git.

No business logic in React components.

No direct database calls from UI components.

No frontend-only authorization.

No untrusted code execution in the main application.

No destructive database migrations without approval.

No undocumented breaking changes.

No claiming tests passed without executing them.

Definition of Done
Every feature must have:

Requirements.

Acceptance criteria.

Implementation.

Unit and integration tests as applicable.

Authorization checks.

Error handling.

Loading and empty states.

Accessibility validation.

Documentation.

Successful CI checks.

3. Technology stack
Recommended stack
Making a custom 404 page in Next.js - DEV Community

Next.js + TypeScript

Frontend, routing, server-side application

Tải mẫu logo Cloudflare file vector AI, EPS, JPEG, SVG, PNG

Cloudflare Workers

Hosting, edge execution, APIs

What is Supabase and why is it used? | by Hatice | Medium

Supabase + PostgreSQL

Database, authentication, storage

Resend Logo Vector File Download | Logowik

Resend

Transactional emails and notifications

Oakstone & Github | Executive Search for GTM SaaS

GitHub

Version control and CI/CD

Additional selections:

Tailwind CSS + shadcn/ui.

Radix UI.

React Hook Form.

Zod.

Drizzle ORM.

Vitest.

Playwright.

OpenTelemetry.

Cloudflare Queues.

Ollama and external LLM APIs.

Hosting consideration: Validate Next.js compatibility with the selected Cloudflare deployment adapter before freezing it. Keep application logic portable to a standard Node.js runtime.

4. System architecture
Recommended architecture:

Modular monolith + ports and adapters + independent tool execution services.

The main platform should not start with dozens of microservices.

Tool Runtimes
Infrastructure
Domain Layer
Application
Cloudflare Workers
External APIs
MCP Servers
Local AI Gateway
PostgreSQL
Email
Object Storage
Job Queue
AI Providers
Identity and Permissions
Tool Management
Project Management
Execution Management
Public Website
Authentication
Workspace
Admin Dashboard
Tool Registry
Execution Router
Visitors and Registered Users
Cloudflare Edge
Next.js Application
Layer responsibilities
Layer

Responsibility

Presentation

Pages, components and user interactions

Application

Use cases and orchestration

Domain

Business rules and entities

Infrastructure

Database, email, storage, queues

Tool runtime

Execute independently registered tools

The domain layer must not import Next.js, Supabase or Cloudflare SDKs.

5. Repository structure
Recommended monorepo:

Portfolio/
│
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .env.example
│
├── apps/
│   ├── web/
│   ├── worker-runtime/
│   ├── background-worker/
│   └── mcp-gateway/
│
├── packages/
│   ├── domain/
│   ├── application/
│   ├── contracts/
│   ├── database/
│   ├── identity/
│   ├── authorization/
│   ├── tool-registry/
│   ├── tool-sdk/
│   ├── tool-runtime/
│   ├── storage/
│   ├── email/
│   ├── queue/
│   ├── ai-providers/
│   ├── observability/
│   ├── ui/
│   └── testing/
│
├── tools/
│   ├── finance/
│   ├── productivity/
│   ├── ai/
│   ├── developer/
│   └── automation/
│
├── infrastructure/
│   ├── cloudflare/
│   ├── database/
│   ├── scripts/
│   └── deployment/
│
├── supabase/
│   ├── migrations/
│   └── seed.sql
│
├── docs/
│   ├── product/
│   ├── architecture/
│   ├── design/
│   ├── security/
│   ├── database/
│   ├── api/
│   ├── integrations/
│   ├── testing/
│   ├── operations/
│   ├── deployment/
│   ├── release/
│   ├── roadmap/
│   └── decisions/
│
├── scripts/
├── tests/
├── pnpm-workspace.yaml
└── package.json
Dependency direction
Presentation
     |
     v
Application
     |
     v
Domain

Infrastructure Adapters
     |
     v
Contracts / Interfaces
Business logic should not depend on vendor implementations.

6. UI/UX design system
Visual direction
Create a premium developer-platform experience inspired by:

Linear's clarity.

Vercel's minimalism.

Raycast's tool discovery.

Stripe's documentation quality.

Do not copy these interfaces.

Design requirements
Dark and light themes.

Consistent typography.

Restrained accent colours.

Consistent spacing.

Responsive layouts.

Subtle animation.

Excellent loading states.

Accessible forms.

Keyboard navigation.

Clear error states.

Consistent iconography.

Avoid excessive gradients, unnecessary animations and inconsistent card layouts.

Design system components
components/
  ui/
    Button
    Input
    Select
    Dialog
    Dropdown
    Tooltip
    Tabs
    Badge
    Avatar
    Skeleton
    Toast
    DataTable

  layout/
    Navbar
    Footer
    Sidebar
    PageHeader
    Breadcrumbs

  tools/
    ToolCard
    ToolHeader
    ToolFilters
    ToolStatus
    ToolLaunchButton
    ToolExecutionPanel

  dashboard/
    StatCard
    ActivityFeed
    RecentTools
Website pages
Page

Function

/

Homepage

/about

Professional profile

/portfolio

Projects

/tools

Tool directory

/tools/[slug]

Individual tool

/workspace

User dashboard

/workspace/tools

Authorized tools

/admin

Admin dashboard

/login

Authentication

/register

Registration

/contact

Contact form

Target WCAG 2.2 AA accessibility.

7. Database design
Use PostgreSQL as the primary database.

Core tables
Table

Purpose

profiles

User profiles

roles

Platform roles

user_roles

User-role relationships

permissions

Permission definitions

role_permissions

Role permissions

projects

Portfolio projects

technologies

Technology catalogue

project_technologies

Project technology mapping

tools

Tool registry

tool_versions

Tool version history

tool_categories

Tool categories

tool_capabilities

Tool capabilities

tool_permissions

Individual access grants

tool_runs

Execution records

tool_run_events

Execution events

tool_favorites

User favorites

notifications

In-app notifications

audit_logs

Security and admin history

Example tool schema
CREATE TABLE tools (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category_id UUID,
    visibility TEXT NOT NULL,
    status TEXT NOT NULL,
    execution_type TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

Database policies
Use UUID primary keys.

Use UTC timestamps.

Enforce foreign keys.

Use explicit indexes.

Maintain migrations in Git.

Enable RLS on user-accessible tables.

Use JSONB only for genuinely flexible configuration.

Keep sensitive documents out of logs.

Maintain ownership for user-generated resources.

Example user-owned record policy:

CREATE POLICY profile_read_own
ON profiles
FOR SELECT
USING (id = auth.uid());

Every table needs policies appropriate to its data ownership and access model. Do not blindly apply the same policy everywhere.

8. Authentication and authorization
Roles
Role

Permissions

Owner

Complete platform control

Admin

Operational management

User

Standard registered access

Visitor

Public access only

Tool visibility
Visibility

Access

Public

Anyone

Authenticated

Registered users

Restricted

Explicitly authorized users

Private

Owner and explicitly authorized users

Authentication flows
Registration
User submits registration.

Validate input.

Apply rate limits.

Create account.

Send verification email.

Verify email.

Create profile.

Assign standard user role.

Redirect to workspace.

Authorization
Every private operation must verify access server-side.

interface AuthorizationService {
  can(
    principal: UserIdentity,
    action: string,
    resource: Resource
  ): Promise<boolean>;
}

Mandatory controls:

Secure sessions.

HTTP-only cookies.

MFA for administrators.

Protected role assignment.

RLS.

Server-side permission checks.

Session revocation.

Audit logs.

Account suspension.

No privilege escalation.

New registrations must never receive administrator or owner privileges automatically.

9. Dynamic tool registry and plugin architecture
This is the most important technical component.

The website must not hardcode individual tools.

Tool manifest
Every tool should expose a manifest.

{
  "schemaVersion": "1.0",
  "id": "finance.stock-pnl",
  "name": "Stock P&L Analyzer",
  "version": "1.0.0",
  "description": "Analyze stock profit and loss reports.",
  "category": "finance",
  "visibility": "authenticated",
  "execution": {
    "type": "api",
    "reference": "stock-pnl-service"
  },
  "capabilities": [
    "document-upload",
    "financial-analysis"
  ]
}

The actual manifest must also define validated input/output schemas, versioning and execution limits.

Do not allow users to submit arbitrary executable URLs.

Tool execution modes
Mode

Example

Embedded

Calculator

Edge

Lightweight parser

API

Existing Java application

Job

Video generation

MCP

Developer automation

Local

Ollama

Standard tool interface
interface ToolExecutor {
  execute(
    input: unknown,
    context: ToolExecutionContext
  ): Promise<ToolExecutionResult>;

  healthCheck(): Promise<HealthStatus>;
}

Tool lifecycle
Draft
  |
Validating
  |
Approved
  |
Published
  |
Disabled
  |
Deprecated
  |
Archived
Publishing requires successful validation, security review, permissions, health check and version identification.

Tool SDK
Create a common SDK containing:

Manifest validation.

Input/output validation.

Authentication context.

Authorization context.

Structured logging.

Error mapping.

Execution tracing.

Idempotency.

File handling.

Testing helpers.

This allows independently developed tools to integrate consistently.

10. API and integration architecture
Use REST with OpenAPI.

Example endpoints:

/api/v1/tools
/api/v1/tools/{slug}
/api/v1/tools/{slug}/execute
/api/v1/executions/{id}
/api/v1/projects
/api/v1/users/me
/api/v1/notifications

/api/v1/admin/users
/api/v1/admin/tools
/api/v1/admin/tools/{id}/publish
/api/v1/admin/tools/{id}/permissions
/api/v1/admin/audit-logs
Standard response:

{
  "success": true,
  "data": {},
  "meta": {
    "requestId": "request-id"
  }
}

API requirements:

Request validation.

Response validation.

Pagination.

Idempotency where appropriate.

Rate limiting.

Timeouts.

Structured errors.

Versioning.

Authorization.

OpenAPI documentation.

Use interfaces and adapters for every external provider.

11. AI, MCP and local AI architecture
AI gateway
AI Gateway
  |
  ├── Model Registry
  ├── Provider Selection
  ├── Request Validation
  ├── Usage Tracking
  ├── Rate Limiting
  ├── Timeout Management
  └── Provider Adapters
        ├── Ollama
        ├── OpenAI-compatible
        ├── Anthropic
        └── Other providers
Provider interface:

interface LLMProvider {
  capabilities(): ProviderCapabilities;

  generate(
    request: LLMRequest
  ): Promise<LLMResponse>;
}

Explicitly model provider capabilities such as streaming, tool calling, image inputs and structured outputs.

MCP gateway
Platform
   |
MCP Gateway
   |
   ├── Server Registry
   ├── Authentication
   ├── Authorization
   ├── Tool Allowlist
   ├── Validation
   ├── Timeouts
   └── Audit Logging
          |
          ├── Approved MCP servers
          ├── Developer utilities
          └── Local MCP services
MCP must not replace the platform's authorization system.

Do not expose confidential Oracle code, logs, telemetry, credentials or internal endpoints.

Local AI
Public Platform
      |
Authenticated Gateway
      |
Private Network / Tailscale
      |
Local AI Gateway
      |
      ├── Ollama
      ├── Local Models
      └── Authorized MCP Servers
Never expose Ollama or MCP services directly to the public internet.

When the local machine is offline, display service unavailability instead of silently failing.

12. Security and privacy policy
Use defence in depth and a zero-trust approach.

Risk

Protection

Account takeover

MFA, secure sessions

Privilege escalation

Server-side role controls

Data leakage

RLS, ownership checks

SQL injection

Parameterized queries

XSS

Output encoding and sanitization

CSRF

Secure cookie/session strategy

SSRF

Outbound destination restrictions

Malicious uploads

Validation and isolated processing

API abuse

Rate limiting and quotas

Secret exposure

Managed secrets

MCP misuse

Allowlist and execution controls

Denial of service

Resource limits and throttling

File upload security
Validate extension.

Validate MIME.

Validate file signature.

Restrict file size.

Use randomized storage names.

Use private buckets.

Use short-lived signed URLs.

Scan files where feasible.

Isolate processing.

Delete temporary files.

Define retention.

Sensitive financial documents
For Form 16, 26AS and Stock P&L:

Do not retain documents by default.

Avoid logging PAN or account information.

Provide deletion controls.

Encrypt retained data.

Restrict access to document processing services.

Minimize external AI provider exposure.

Release security gate
Mandatory release blocker
No release with unresolved critical or high-severity security issues, exposed secrets, broken authorization or unauthorized private tool execution.

13. Email and notification architecture
Use an EmailProvider abstraction.

Initial provider: Resend.

Potential replacements: SES, Postmark and SMTP.

Email events
Registration verification.

Password reset.

Welcome email.

User invitation.

Access granted.

Access revoked.

Tool completion.

Security alerts.

Contact form notification.

Professional email
Initially, use your existing Gmail address and transactional email testing.

After buying a domain:

hello@yourdomain.com
support@yourdomain.com
notifications@yourdomain.com
Configure:

SPF.

DKIM.

DMARC.

Incoming email forwarding or a mailbox.

Verified transactional sender.

Cloudflare Email Routing forwards incoming messages; it does not itself provide a full mailbox.

14. Background jobs and execution
Do not make users wait for long-running processing.

Use asynchronous jobs for:

Large PDF processing.

AI generation.

Video generation.

Bulk processing.

Automation.

External workflows.

User Request
    |
Authorization
    |
Create Job
    |
Queue
    |
Background Worker
    |
Tool Runtime
    |
Update Status
    |
Notify User
Job states:

CREATED
QUEUED
RUNNING
COMPLETED
FAILED
CANCELLED
TIMED_OUT
Mandatory features:

Idempotency.

Retry limits.

Exponential backoff.

Dead-letter handling.

Timeouts.

Cancellation.

Progress updates.

User concurrency limits.

Use Cloudflare Queues where compatible. Heavy GPU/CPU workloads should run separately.

15. Observability and operations
Implement structured JSON logging.

Example:

{
  "level": "INFO",
  "service": "tool-executor",
  "requestId": "request-123",
  "toolId": "finance.stock-pnl",
  "event": "execution.completed",
  "durationMs": 1250
}

Never log passwords, access tokens, API keys or complete sensitive documents.

Track:

Metric

Purpose

Request count

Usage

Error rate

Reliability

Latency

Performance

Login failures

Security

Tool execution time

Performance

Queue depth

Backlog

Failed jobs

Reliability

Storage usage

Capacity

Email delivery failures

Communications

Use OpenTelemetry for traces and standardized instrumentation.

Create:

/health
/health/ready
/health/live
Also implement:

Error monitoring.

Security alerts.

Backup monitoring.

Incident runbooks.

Cost monitoring.

16. Testing strategy
Use a testing pyramid.

Unit Tests
Integration Tests
Contract Tests
End-to-End Tests
Security Tests
Release Confidence
Test category

Technology

Unit

Vitest

Component

Testing Library

E2E

Playwright

Accessibility

axe-core

API contracts

OpenAPI/schema tests

Security

OWASP ZAP and targeted tests

Load

k6

Database

PostgreSQL test environment

Critical E2E scenarios:

Visitor opens homepage.

Visitor browses public tools.

Visitor registers.

User verifies email.

User logs in.

User executes a public tool.

User attempts a private tool and is denied.

Admin grants access.

User executes the private tool.

Admin revokes access.

User loses access.

Password recovery works.

User logs out.

Target 90%+ test coverage for domain and authorization logic, with meaningful integration and contract coverage.

17. CI/CD and deployment
Git workflow
main
  |
  ├── feature/authentication
  ├── feature/tool-registry
  ├── feature/portfolio
  ├── feature/admin-dashboard
  └── fix/authorization
Use pull requests and short-lived branches.

CI pipeline
Every pull request must run:

Prettier.

ESLint.

TypeScript checks.

Unit tests.

Integration tests.

Architecture checks.

Dependency security scans.

Secret scanning.

Production build.

Preview deployment.

E2E tests.

Accessibility tests.

Environments
Environment

Purpose

Local

Development

Test

Automated testing

Staging

Release verification

Production

Real users

Keep separate secrets, credentials and storage for each environment.

Initial deployment cost
Service

Initial cost

Cloudflare hosting

₹0

Supabase Free

₹0

Resend Free

₹0

GitHub Free

₹0

Free subdomain

₹0

Local Ollama

₹0 additional

Custom domain

Deferred

Free-tier limits apply. Supabase Free projects can pause after inactivity and do not include automatic backups. Cloudflare Workers free requests have execution limits. Validate current provider terms before production release.

Backup strategy
Encrypted database exports.

Storage metadata backups.

Migration history in Git.

Recovery documentation.

Restoration testing.

Credential recovery process.

Rollback procedures.

Initial recovery objectives: maximum 24-hour RPO and four-hour RTO, with better targets as the platform grows.

18. Implementation roadmap
Follow this sequence. Do not implement everything simultaneously.

Complete development roadmap
Phase 0 — Discovery

Inspect Portfolio directory.

Inventory existing projects.

Inspect agent skills.

Identify reusable components.

Identify dependencies.

Identify security risks.

Approve initial scope.

Deliverable: Repository inventory and risk assessment.

Phase 1 — Foundation

Create monorepo.

Configure pnpm.

Configure TypeScript.

Create shared packages.

Establish dependency boundaries.

Configure CI/CD.

Create database migrations.

Deploy initial application.

Deliverable: Working application and deployment.

Phase 2 — Design system and public website

Finalize visual direction.

Build design tokens.

Build components.

Build homepage.

Build About page.

Build portfolio.

Build tools directory.

Build contact form.

Implement accessibility and SEO.

Deliverable: Complete responsive public website.

Phase 3 — Authentication and security

Supabase Auth.

Registration/login.

Email verification.

Password recovery.

User profiles.

Roles and permissions.

RLS.

MFA.

Audit logs.

Deliverable: Secure multi-user foundation.

Phase 4 — Tool registry and administration

Tool manifest.

Tool categories.

Tool versions.

Search and filters.

Admin tool manager.

Visibility controls.

User permissions.

Publishing workflow.

Deliverable: Dynamic tool marketplace.

Phase 5 — Execution engine

Execution router.

Runtime adapters.

API integration.

Worker integration.

Background queues.

Execution history.

Quotas and timeouts.

Deliverable: Independent tool execution framework.

Phase 6 — Integrations

Email provider.

Storage provider.

AI gateway.

Ollama.

MCP gateway.

External APIs.

Local AI gateway.

Deliverable: Integrated AI and developer ecosystem.

Phase 7 — Existing tools

Audit each existing tool.

Build adapters.

Add tests.

Register manifests.

Configure permissions.

Publish approved tools.

Deliverable: Existing applications integrated.

Phase 8 — Operational readiness

Logging.

Monitoring.

Backup.

Restore tests.

Performance testing.

Security testing.

Documentation.

Deliverable: Production-ready operational foundation.

Phase 9 — Release candidate

Full regression.

Accessibility audit.

Security review.

Mobile testing.

Recovery test.

Deployment verification.

Deliverable: Approved release candidate.

Phase 10 — Production release

Publish website.

Enable registration.

Publish approved tools.

Configure monitoring.

Gather feedback.

Fix launch issues.

Deliverable: Publicly available platform.

19. Agent-driven development policy
This platform should be understandable to Codex, Claude Code, Gemini CLI and other compatible agents.

Agent roles
Role

Responsibility

Architect

Architecture and design decisions

Product analyst

Requirements

UI/UX

Visual design and accessibility

Frontend

Next.js and UI

Backend

Business logic and APIs

Database

Schema and migrations

Security

Threat modelling and security

QA

Automated tests

DevOps

CI/CD and hosting

Reviewer

Independent review

Mandatory agent instructions
Create AGENTS.md in the root.

# Project Instructions

1. Read README.md and AGENTS.md.
2. Read relevant architecture documentation.
3. Inspect existing code before modifying anything.
4. Check Git status.
5. Never overwrite existing work without approval.

## Architecture
- Follow modular architecture.
- Respect dependency boundaries.
- Use provider interfaces.
- Keep domain logic framework-independent.
- Avoid unnecessary microservices.

## Security
- Deny by default.
- Verify permissions server-side.
- Validate all inputs.
- Never expose secrets.
- Protect user-owned resources.
- Never bypass RLS.

## UI
- Follow the central design system.
- Maintain responsiveness.
- Maintain accessibility.
- Implement loading and error states.

## Testing
- Add tests for new business logic.
- Add authorization regression tests.
- Run relevant tests.
- Never claim tests passed without execution.

## Database
- Use migrations.
- Never make undocumented schema changes.
- Do not perform destructive production operations.

## Documentation
- Update docs with implementation changes.
- Record major decisions in ADRs.
- Document environment variables.

## Completion report
- Changes made.
- Files modified.
- Tests executed.
- Results.
- Security implications.
- Known limitations.
- Follow-up tasks.
Superpowers workflow
If obra/superpowers is installed, use the relevant available skills:

Activity

Skill workflow

Feature exploration

Brainstorming

Implementation planning

Writing plans

Implementation

Executing plans

Bug fixing

Systematic debugging

Test-first development

Test-driven development

Final validation

Verification before completion

Code review

Requesting code review

Follow the exact installed skill instructions rather than assuming identical versions across agents.

Agent workflow
Receive Task
Read Instructions
Inspect Existing Code
Understand Requirements
Create Plan
Review Architecture
Implement Tests
Implement Feature
Run Verification
Passed?
Fix Issues
Independent Review
Update Documentation
Completion Report
No
Yes
For parallel agents:

Assign separate modules.

Define interfaces before parallel work.

Use separate branches.

Avoid simultaneous migration changes.

Review integration changes.

Never let multiple agents independently change shared architecture without approval.

20. Documentation structure
Maintain all engineering documentation in the repository.

docs/
│
├── 00-MASTER-PLAN.md
│
├── product/
│   ├── requirements.md
│   ├── personas.md
│   └── user-journeys.md
│
├── architecture/
│   ├── system-architecture.md
│   ├── application-architecture.md
│   ├── module-boundaries.md
│   └── integration-architecture.md
│
├── design/
│   ├── visual-direction.md
│   ├── design-tokens.md
│   ├── components.md
│   └── accessibility.md
│
├── security/
│   ├── security-policy.md
│   ├── threat-model.md
│   ├── authentication.md
│   ├── authorization.md
│   └── privacy.md
│
├── database/
│   ├── schema.md
│   ├── relationships.md
│   └── backup-recovery.md
│
├── integrations/
│   ├── provider-contracts.md
│   ├── email.md
│   ├── ai.md
│   ├── mcp.md
│   └── local-ai.md
│
├── testing/
│   ├── testing-strategy.md
│   └── security-testing.md
│
├── operations/
│   ├── monitoring.md
│   ├── logging.md
│   └── incident-response.md
│
├── deployment/
│   ├── environments.md
│   ├── ci-cd.md
│   └── release.md
│
├── roadmap/
│   ├── milestones.md
│   ├── backlog.md
│   └── progress.md
│
└── decisions/
    ├── ADR-001-modular-architecture.md
    ├── ADR-002-database.md
    ├── ADR-003-authentication.md
    ├── ADR-004-tool-execution.md
    ├── ADR-005-hosting.md
    └── ADR-006-provider-abstraction.md
ADR format
Every major architecture decision should record:

# ADR-XXX: Decision title

## Status

Proposed / Accepted / Superseded

## Context

Why is this decision needed?

## Decision

What is being selected?

## Alternatives

What else was considered?

## Consequences

Benefits and limitations.

## Migration Strategy

How can this be replaced?

## Security Implications

What risks does it introduce?
21. Acceptance criteria
The platform is not ready for release until these requirements are satisfied.

Public website

Homepage works.

Portfolio is dynamic.

Tools directory is searchable.

Public tools work without login.

Private tools are protected.

Mobile layouts work.

SEO is configured.

Accessibility checks pass.
Authentication

Registration works.

Email verification works.

Login/logout works.

Password recovery works.

Admin MFA works.

Privilege escalation is prevented.

Cross-user access is prevented.
Tool ecosystem

Tools can be registered dynamically.

Manifests are validated.

Tools can be versioned.

Permissions can be granted and revoked.

Execution status is visible.

Multiple execution modes work.

Adapter contract tests pass.
Infrastructure

Migrations are reproducible.

Backups work.

Restore is tested.

Email works.

CI/CD works.

Staging works.

Production deployment works.

Monitoring is available.
Agent readiness

AGENTS.md exists.

Architecture documents exist.

ADRs are maintained.

Agent workflow is documented.

Progress tracking exists.

Independent reviews are possible.
22. Future evolution
Prepare for these features, but do not build them in the initial release.

Feature

Future capability

Subscriptions

Free, Pro, Enterprise

Billing

Payment gateway adapter

API marketplace

Developer API keys

Teams

Organizations and memberships

External developers

Tool publishing

Marketplace

Tool submissions and approval

Agent ecosystem

Agent runtime

Advanced analytics

Usage analytics

Mobile application

Shared API and identity

SDK

External tool integrations

Future entitlement structure:

Plans
  |
  ├── Free
  ├── Pro
  └── Enterprise

Entitlements
  |
  ├── Tool access
  ├── Execution limits
  ├── Storage limits
  ├── AI usage
  └── API access
23. Initial tool catalogue
Based on your existing projects, I recommend starting with these categories.

Category

Candidate tools

Finance

Form 16 Parser, 26AS Parser, Stock P&L Analyzer

Productivity

PDF Analyzer, Document Extractor

AI

AI Story Generator, Content Assistant

Developer

MCP Playground, API Utilities

Automation

Workflow Automation, Data Processing

For each portfolio project, publish:

Problem statement.

Solution.

Architecture.

Technology stack.

Engineering decisions.

Challenges.

Performance improvements.

Business impact.

Screenshots.

Demo URL.

GitHub URL, if public.

Only publish professional work that you are authorized to disclose.

24. Initial architecture decision register
These are proposed decisions, subject to validation during discovery.

ID

Decision

ADR-001

Modular monolith initially

ADR-002

PostgreSQL as primary database

ADR-003

Supabase Auth initially

ADR-004

Next.js + TypeScript

ADR-005

Cloudflare hosting initially

ADR-006

Ports and adapters

ADR-007

Dynamic tool registry

ADR-008

Independent tool runtimes

ADR-009

REST + OpenAPI

ADR-010

Central design system

ADR-011

RBAC + resource-level permissions

ADR-012

Independent MCP integration layer

ADR-013

Resend email provider

ADR-014

GitHub CI/CD

ADR-015

Automated backup and recovery

25. First development backlog
This is the exact order I would start implementing.

Task

Priority

Inspect existing Portfolio directory

P0

Inventory existing projects

P0

Inspect available agent skills

P0

Inventory reusable components

P0

Approve architecture

P0

Establish AGENTS.md

P0

Create ADRs

P0

Initialize monorepo

P0

Configure CI/CD

P0

Build design system

P0

Create database schema

P0

Implement authentication

P0

Implement authorization

P0

Build public website

P0

Build tool registry

P0

Build admin dashboard

P1

Build execution router

P0

Integrate first sample tool

P0

Integrate email

P1

Integrate existing tools

P1

Integrate MCP

P2

Integrate Ollama

P2

Complete security testing

P0

Production release

P0

26. Final execution strategy
The complete journey
Discover existing projects and agent resources.
Finalize requirements and architecture.
Establish engineering policies and repository structure.
Build the design system and public experience.
Implement authentication, authorization and security.
Build the tool registry and admin dashboard.
Build independent execution infrastructure.
Integrate existing projects, AI and MCP.
Validate reliability, security and performance.
Deploy and release the platform.
My final recommendations
Five principles should never be compromised:

Security first: Every private tool must enforce access independently.

Provider independence: External infrastructure must be replaceable through adapters.

Tool independence: Tools should not depend on the website's internal implementation.

Design consistency: Every application should feel like part of the same product.

Agent governance: Agents must follow documented architecture, testing and review policies.

The final outcome should allow you to develop your 10th or 50th tool independently, register it, assign permissions and publish it without rebuilding the central platform.

The first action should be Phase 0: inspect and inventory everything already present in /Users/admin/Downloads/Portfolio. Do not start by rewriting existing projects or generating the entire application in one shot.

This blueprint defines the target architecture and release process. Actual provider compatibility, existing-project reuse and security decisions must be verified during discovery before implementation begins.





.

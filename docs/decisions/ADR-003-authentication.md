# ADR-003: Supabase Auth with Server-Side RBAC

## Context

In the context of the Personal Technology Platform, we need to implement authentication using Supabase, a PostgreSQL-based database and authentication service. The platform will utilize Server-side Role-Based Access Control (RBAC) to manage user permissions and ensure that only authenticated users can access certain features.

## Decision

We will use Supabase for authentication and implement Server-side RBAC to manage user roles and permissions. The authentication process will involve the following steps:

1. User logs in via email or social media.
2. Supabase handles the authentication and stores the user's session.
3. The platform will validate the session and check the user's role.
4. Based on the user's role, the platform will grant or deny access to specific features.

## Consequences

- **Positive:** 
  - Improved security through Supabase's built-in authentication features.
  - Centralized authentication and authorization management.
  - Enhanced user experience with seamless login and access control.
  
- **Negative:** 
  - Potential performance impact due to additional database calls for authentication.
  - Complexity in managing roles and permissions.
  - Potential for security vulnerabilities if not implemented correctly.

## Implementation Details

### 1. Authentication Setup

- **Supabase Setup:** 
  - Create a Supabase project and configure it to use PostgreSQL.
  - Set up email and social media authentication providers.
  - Configure Supabase to store user sessions securely.

- **Supabase API Endpoints:**
  - `POST /supabase/auth/login`: Handles user login via email or social media.
  - `GET /supabase/auth/session`: Validates user session and returns user information.

### 2. Server-Side RBAC

- **Role Definitions:**
  - Define roles such as `user`, `admin`, `developer`, etc.
  - Assign roles to users based on their account creation or other criteria.

- **Role-Based Access Control:**
  - Implement middleware to check user roles before accessing protected routes.
  - Use role-based permissions to control access to specific features.

### 3. Database Schema

- **Users Table:**
  - `id`: UUID, primary key.
  - `email`: String, unique.
  - `password`: String, hashed.
  - `role`: Enum, e.g., `user`, `admin`, `developer`.
  - `session_token`: String, for storing session tokens.

- **Permissions Table:**
  - `id`: UUID, primary key.
  - `user_id`: Foreign key referencing `Users` table.
  - `feature`: String, e.g., `read`, `write`, `admin`.
  - `level`: Enum, e.g., `read`, `write`, `admin`.

### 4. Security Considerations

- **Password Hashing:** Use a strong hashing algorithm (e.g., bcrypt) to store passwords securely.
- **Session Management:** Implement session expiration and token revocation to prevent session hijacking.
- **Rate Limiting:** Implement rate limiting to prevent brute force attacks.
- **Audit Logs:** Maintain audit logs for authentication and authorization activities.

### 5. Testing

- **Unit Tests:** Test individual components of the authentication and RBAC system.
- **Integration Tests:** Test the interaction between Supabase and the platform.
- **Security Tests:** Perform security audits to identify and mitigate potential vulnerabilities.

### 6. Deployment

- **CI/CD Pipeline:** Set up a CI/CD pipeline to automate the deployment of authentication and RBAC components.
- **Monitoring:** Monitor the system for performance and security issues.

### 7. Documentation

- **User Guide:** Provide documentation on how to use the authentication and RBAC system.
- **Developer Guide:** Provide detailed information on the implementation and usage of the authentication and RBAC system.

## References

- [Supabase Documentation](https://supabase.io/docs/guides/auth)
- [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control)
- [Authentication and Authorization Best Practices](https://auth0.com/blog/authentication-and-authorization-best-practices/)

---

This document outlines the decision to use Supabase for authentication and implement Server-side RBAC for managing user roles and permissions. It includes details on the implementation, security considerations, testing, deployment, and documentation.

# docs/database/schema.md

## Overview
This document describes the PostgreSQL database schema for the Personal Technology Platform. It includes the structure and definitions for the following tables: `profiles`, `roles`, `user_roles`, `tools`, `tool_versions`, `tool_runs`, `notifications`, and `audit_logs`.

## Tables

### Profiles
- **Table Name:** profiles
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each profile.
  - `user_id` (INT, FOREIGN KEY): The user ID associated with this profile.
  - `name` (VARCHAR): The name of the profile.
  - `description` (TEXT): A description of the profile.
  - `created_at` (TIMESTAMP): The timestamp when the profile was created.
  - `updated_at` (TIMESTAMP): The timestamp when the profile was last updated.

### Roles
- **Table Name:** roles
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each role.
  - `name` (VARCHAR): The name of the role.
  - `description` (TEXT): A description of the role.
  - `created_at` (TIMESTAMP): The timestamp when the role was created.
  - `updated_at` (TIMESTAMP): The timestamp when the role was last updated.

### User_Roles
- **Table Name:** user_roles
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each user role association.
  - `user_id` (INT, FOREIGN KEY): The user ID associated with this role.
  - `role_id` (INT, FOREIGN KEY): The role ID associated with this user role association.
  - `created_at` (TIMESTAMP): The timestamp when the user role association was created.
  - `updated_at` (TIMESTAMP): The timestamp when the user role association was last updated.

### Tools
- **Table Name:** tools
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each tool.
  - `name` (VARCHAR): The name of the tool.
  - `description` (TEXT): A description of the tool.
  - `created_at` (TIMESTAMP): The timestamp when the tool was created.
  - `updated_at` (TIMESTAMP): The timestamp when the tool was last updated.

### Tool_Versions
- **Table Name:** tool_versions
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each tool version.
  - `tool_id` (INT, FOREIGN KEY): The tool ID associated with this version.
  - `version` (VARCHAR): The version of the tool.
  - `created_at` (TIMESTAMP): The timestamp when the tool version was created.
  - `updated_at` (TIMESTAMP): The timestamp when the tool version was last updated.

### Tool_Runs
- **Table Name:** tool_runs
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each tool run.
  - `tool_version_id` (INT, FOREIGN KEY): The tool version ID associated with this run.
  - `user_id` (INT, FOREIGN KEY): The user ID associated with this run.
  - `profile_id` (INT, FOREIGN KEY): The profile ID associated with this run.
  - `status` (VARCHAR): The status of the tool run (e.g., "completed", "in progress", "failed").
  - `created_at` (TIMESTAMP): The timestamp when the tool run was created.
  - `updated_at` (TIMESTAMP): The timestamp when the tool run was last updated.

### Notifications
- **Table Name:** notifications
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each notification.
  - `user_id` (INT, FOREIGN KEY): The user ID associated with this notification.
  - `message` (TEXT): The message of the notification.
  - `status` (VARCHAR): The status of the notification (e.g., "unread", "read").
  - `created_at` (TIMESTAMP): The timestamp when the notification was created.
  - `updated_at` (TIMESTAMP): The timestamp when the notification was last updated.

### Audit_Logs
- **Table Name:** audit_logs
- **Columns:**
  - `id` (INT, PRIMARY KEY, AUTO_INCREMENT): A unique identifier for each audit log entry.
  - `user_id` (INT, FOREIGN KEY): The user ID associated with this log entry.
  - `action` (VARCHAR): The action performed (e.g., "profile created", "tool run started").
  - `details` (TEXT): Additional details about the action.
  - `created_at` (TIMESTAMP): The timestamp when the log entry was created.
  - `updated_at` (TIMESTAMP): The timestamp when the log entry was last updated.

## Foreign Key Constraints
- `user_id` in `profiles`, `user_roles`, `tool_runs`, `notifications`, `audit_logs` references `id` in `users`.
- `role_id` in `user_roles` references `id` in `roles`.
- `tool_version_id` in `tool_runs` references `id` in `tool_versions`.
- `tool_id` in `tool_versions` references `id` in `tools`.

## Indexes
- `profiles` table: `user_id`, `name`, `created_at`, `updated_at`
- `roles` table: `name`, `created_at`, `updated_at`
- `user_roles` table: `user_id`, `role_id`, `created_at`, `updated_at`
- `tools` table: `name`, `created_at`, `updated_at`
- `tool_versions` table: `tool_id`, `version`, `created_at`, `updated_at`
- `tool_runs` table: `user_id`, `profile_id`, `tool_version_id`, `status`, `created_at`, `updated_at`
- `notifications` table: `user_id`, `status`, `created_at`, `updated_at`
- `audit_logs` table: `user_id`, `action`, `created_at`, `updated_at`

## Conclusion
This schema provides a robust foundation for the Personal Technology Platform, enabling efficient management of user profiles, roles, tool versions, and audit logs. It ensures data integrity and supports various operations such as user profile management, tool versioning, and notification handling.

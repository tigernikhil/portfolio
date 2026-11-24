export class ToolExecutionError extends Error {
  code: string;
  statusCode: number;
  details?: unknown;

  constructor(message: string, code: string, statusCode: number, details?: unknown) {
    super(message);
    this.code = code;
    this.statusCode = statusCode;
    this.details = details;
    Object.setPrototypeOf(this, ToolExecutionError.prototype);
  }
}

export class ManifestValidationError extends ToolExecutionError {
  constructor(message: string, details?: unknown) {
    super(message, 'ERR_INVALID_MANIFEST', 400, details);
    Object.setPrototypeOf(this, ManifestValidationError.prototype);
  }
}

export class PermissionDeniedError extends ToolExecutionError {
  constructor(message: string, details?: unknown) {
    super(message, 'ERR_PERMISSION_DENIED', 403, details);
    Object.setPrototypeOf(this, PermissionDeniedError.prototype);
  }
}

export class RateLimitExceededError extends ToolExecutionError {
  constructor(message: string, details?: unknown) {
    super(message, 'ERR_RATE_LIMIT_EXCEEDED', 429, details);
    Object.setPrototypeOf(this, RateLimitExceededError.prototype);
  }
}

export class ServiceUnavailableError extends ToolExecutionError {
  constructor(message: string, details?: unknown) {
    super(message, 'ERR_SERVICE_UNAVAILABLE', 503, details);
    Object.setPrototypeOf(this, ServiceUnavailableError.prototype);
  }
}

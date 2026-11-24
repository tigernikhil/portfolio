# docs/design/design-tokens.md

## Design Tokens Overview

This document outlines the design tokens for the Personal Technology Platform, which are used to define the colors, spacing, typography scale, radii, shadows, and transitions. These tokens are based on the principles of Tailwind CSS, a utility-first CSS framework.

## Design Tokens

### Colors

Colors are defined using Tailwind's utility classes. Here are the primary and secondary colors used in the platform.

| Color Name | Tailwind Class | Hex Code |
|------------|----------------|----------|
| Primary    | text-primary    | #007bff   |
| Secondary  | text-secondary  | #6c757d   |

### Spacing

Spacing is defined using Tailwind's utility classes. Here are the spacing values used in the platform.

| Spacing Name | Tailwind Class | Value |
|--------------|----------------|-------|
| S            | text-s          | 0.5rem |
| M            | text-m          | 1rem   |
| L            | text-l          | 1.5rem |
| XL           | text-xl         | 2rem   |

### Typography Scale

Typography scale is defined using Tailwind's utility classes. Here are the typography scale values used in the platform.

| Scale Name | Tailwind Class | Value |
|------------|----------------|-------|
| S          | text-s          | 0.875rem |
| M          | text-m          | 1rem   |
| L          | text-l          | 1.125rem |
| XL         | text-xl         | 1.25rem |

### Radii

Radii are defined using Tailwind's utility classes. Here are the radii values used in the platform.

| Radius Name | Tailwind Class | Value |
|-------------|----------------|-------|
| S           | rounded-s       | 0.25rem |
| M           | rounded-m       | 0.5rem |
| L           | rounded-l       | 0.75rem |
| XL          | rounded-xl      | 1rem   |

### Shadows

Shadows are defined using Tailwind's utility classes. Here are the shadow values used in the platform.

| Shadow Name | Tailwind Class | Value |
|-------------|----------------|-------|
| S           | shadow-s        | 0.25rem |
| M           | shadow-m        | 0.5rem |
| L           | shadow-l        | 0.75rem |
| XL          | shadow-xl       | 1rem   |

### Transitions

Transitions are defined using Tailwind's utility classes. Here are the transition values used in the platform.

| Transition Name | Tailwind Class | Value |
|-----------------|----------------|-------|
| S               | transition-s   | 0.125s |
| M               | transition-m   | 0.25s  |
| L               | transition-l   | 0.5s   |
| XL              | transition-xl  | 0.75s  |

## Production-Ready Usage

To use these design tokens in your code, you can import them into your Tailwind configuration file. Here is an example of how to import the design tokens:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#007bff',
        secondary: '#6c757d',
      },
      spacing: {
        S: '0.5rem',
        M: '1rem',
        L: '1.5rem',
        XL: '2rem',
      },
      radius: {
        S: '0.25rem',
        M: '0.5rem',
        L: '0.75rem',
        XL: '1rem',
      },
      boxShadow: {
        S: '0.25rem',
        M: '0.5rem',
        L: '0.75rem',
        XL: '1rem',
      },
      transitionDuration: {
        S: '0.125s',
        M: '0.25s',
        L: '0.5s',
        XL: '0.75s',
      },
    },
  },
};
```

## Conclusion

This document provides a comprehensive overview of the design tokens for the Personal Technology Platform, including colors, spacing, typography scale, radii, shadows, and transitions. These tokens are based on the principles of Tailwind CSS and are designed to be production-ready for use in the platform.

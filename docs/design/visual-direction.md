# Visual Direction Documentation

## Overview
This document outlines the visual direction for the Personal Technology Platform, inspired by the design principles of Linear, Vercel, Raycast, and Stripe. It includes details on typography, theme options (dark and light), and the color palette to ensure a cohesive and user-friendly experience.

## Typography
The typography will be consistent across the platform to ensure readability and consistency. The following fonts will be used:

- **Primary Font:** Montserrat (for headings)
- **Secondary Font:** Open Sans (for body text)

### Font Sizes
- **Heading 1 (H1):** 32px
- **Heading 2 (H2):** 24px
- **Heading 3 (H3):** 20px
- **Heading 4 (H4):** 18px
- **Body Text (P):** 16px

### Line Heights
- **Heading 1 (H1):** 1.5
- **Heading 2 (H2):** 1.5
- **Heading 3 (H3):** 1.5
- **Heading 4 (H4):** 1.5
- **Body Text (P):** 1.5

## Theme Options
The platform will offer two theme options: Dark and Light. These themes will be applied to all user interfaces to provide a consistent and user-friendly experience.

### Dark Theme
- Background Color: #121212
- Text Color: #FFFFFF
- Links: #007BFF
- Borders: #444444

### Light Theme
- Background Color: #F5F5F5
- Text Color: #000000
- Links: #0056B3
- Borders: #E0E0E0

## Color Palette
The following color palette will be used to ensure consistency and brand recognition across the platform.

### Primary Colors
- **Primary Color 1:** #007BFF
- **Primary Color 2:** #FF6F00
- **Primary Color 3:** #00B0F0

### Secondary Colors
- **Secondary Color 1:** #FFCC00
- **Secondary Color 2:** #FF4D46
- **Secondary Color 3:** #00B0F0

### Accent Colors
- **Accent Color 1:** #FF6F00
- **Accent Color 2:** #00B0F0

## Production-Ready Specifications
The following specifications are designed to be production-ready and should be implemented in the platform's design system.

### Dark Theme CSS
```css
/* Dark Theme */
body {
    background-color: #121212;
    color: #FFFFFF;
}

a {
    color: #007BFF;
}

a:hover {
    color: #0056B3;
}

/* Borders */
border-color: #444444;
```

### Light Theme CSS
```css
/* Light Theme */
body {
    background-color: #F5F5F5;
    color: #000000;
}

a {
    color: #0056B3;
}

a:hover {
    color: #007BFF;
}

/* Borders */
border-color: #E0E0E0;
```

### Color Palette CSS
```css
/* Primary Colors */
.primary-color-1 {
    background-color: #007BFF;
    color: #007BFF;
}

.primary-color-2 {
    background-color: #FF6F00;
    color: #FF6F00;
}

.primary-color-3 {
    background-color: #00B0F0;
    color: #00B0F0;
}

/* Secondary Colors */
.secondary-color-1 {
    background-color: #FFCC00;
    color: #FFCC00;
}

.secondary-color-2 {
    background-color: #FF4D46;
    color: #FF4D46;
}

.secondary-color-3 {
    background-color: #00B0F0;
    color: #00B0F0;
}

/* Accent Colors */
.accent-color-1 {
    background-color: #FF6F00;
    color: #FF6F00;
}

.accent-color-2 {
    background-color: #00B0F0;
    color: #00B0F0;
}
```

## Conclusion
This comprehensive documentation provides a clear and detailed specification for the visual direction of the Personal Technology Platform. By following these guidelines, the platform will maintain a consistent and professional look, enhancing user experience and brand recognition.

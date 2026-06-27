import React from 'react'
import { colors, borderRadius } from '@/lib/design-system'

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  loading?: boolean
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', loading, children, className, ...props }, ref) => {
    const baseStyles = `
      font-medium transition-all duration-200 font-sans
      disabled:opacity-50 disabled:cursor-not-allowed
      ${loading ? 'opacity-50 cursor-not-allowed' : ''}
    `

    const variantStyles = {
      primary: `bg-[${colors.primary.main}] text-white hover:bg-[${colors.primary.dark}]`,
      secondary: `bg-white border border-[${colors.primary.main}] text-[${colors.primary.main}] hover:bg-[${colors.primary.light}]`,
      danger: `bg-red-500 text-white hover:bg-red-600`,
    }

    const sizeStyles = {
      sm: 'px-3 py-2 text-sm',
      md: 'px-4 py-2 text-base',
      lg: 'px-6 py-3 text-lg',
    }

    return (
      <button
        ref={ref}
        className={`
          ${baseStyles}
          ${variantStyles[variant]}
          ${sizeStyles[size]}
          rounded-lg
          ${className}
        `}
        disabled={loading || props.disabled}
        {...props}
      >
        {loading ? '...' : children}
      </button>
    )
  }
)

Button.displayName = 'Button'

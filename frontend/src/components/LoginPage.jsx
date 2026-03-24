import { useState } from 'react'
import './LoginPage.css'
import logo from '../assets/wonder-learning-logo.png'

const ADMIN_EMAIL = 'pramod.wonderlearning@gmail.com'
const ADMIN_PASSWORD = 'Pramod@1309'

const LoginPage = () => {
  const [activeTab, setActiveTab] = useState('admin')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleLogin = (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    if (activeTab === 'admin') {
      const matchesAdmin =
        email.trim().toLowerCase() === ADMIN_EMAIL.toLowerCase() &&
        password === ADMIN_PASSWORD

      if (matchesAdmin) {
        // In this frontend-only setup we just show success.
        setLoading(false)
        alert('Admin login successful.')
        return
      }

      setLoading(false)
      setError('Invalid admin credentials.')
      return
    }

    setLoading(false)
    setError('School login will be enabled after admin creates credentials.')
  }

  return (
    <div className="login-container">
      <div className="login-left">
        <div className="login-info">
          <div className="logo-container">
            <img src={logo} alt="Wonder Learning Logo" className="company-logo" />
          </div>
          <h1 className="library-title">Wonder Learning Digital Library</h1>
          <div className="info-content">
            <p className="info-subtitle">Empowering Schools Through Digital Education</p>
            <div className="info-points">
              <div className="info-point">
                <span>Access to thousands of digital resources</span>
              </div>
              <div className="info-point">
                <span>Secure and easy-to-use platform</span>
              </div>
              <div className="info-point">
                <span>Designed specifically for schools</span>
              </div>
              <div className="info-point">
                <span>24/7 access to educational materials</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="login-right">
        <div className="login-box">
          <h2 className="login-title">Login to Your Account</h2>

          <div className="tabs">
            <button
              className={`tab ${activeTab === 'admin' ? 'active' : ''}`}
              onClick={() => {
                setActiveTab('admin')
                setError('')
                setEmail('')
                setPassword('')
              }}
            >
              Admin Login
            </button>
            <button
              className={`tab ${activeTab === 'school' ? 'active' : ''}`}
              onClick={() => {
                setActiveTab('school')
                setError('')
                setEmail('')
                setPassword('')
              }}
            >
              School Login
            </button>
          </div>

          <form onSubmit={handleLogin}>
            {error && <div className="error-message">{error}</div>}

            <div className="form-group">
              <label htmlFor="email">Email Address</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                placeholder="Enter your email"
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                placeholder="Enter your password"
              />
            </div>

            <button type="submit" className="login-btn" disabled={loading}>
              {loading ? 'Logging in...' : 'Login'}
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default LoginPage

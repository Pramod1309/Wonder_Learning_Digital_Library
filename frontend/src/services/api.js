const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

class ApiService {
  async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      if (response.status === 204) {
        return null;
      }
      
      return await response.json();
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  // Books API
  async getBooks(skip = 0, limit = 100) {
    return this.request(`/books?skip=${skip}&limit=${limit}`);
  }

  async getBook(bookId) {
    return this.request(`/books/${bookId}`);
  }

  async createBook(bookData) {
    return this.request('/books', {
      method: 'POST',
      body: JSON.stringify(bookData),
    });
  }

  async updateBook(bookId, bookData) {
    return this.request(`/books/${bookId}`, {
      method: 'PUT',
      body: JSON.stringify(bookData),
    });
  }

  async deleteBook(bookId) {
    return this.request(`/books/${bookId}`, {
      method: 'DELETE',
    });
  }

  async searchBooks(query, skip = 0, limit = 100) {
    return this.request(`/books/search?q=${encodeURIComponent(query)}&skip=${skip}&limit=${limit}`);
  }

  async getBooksByCategory(category, skip = 0, limit = 100) {
    return this.request(`/books/category/${encodeURIComponent(category)}?skip=${skip}&limit=${limit}`);
  }

  // Health check
  async healthCheck() {
    return this.request('/');
  }
}

export const apiService = new ApiService();

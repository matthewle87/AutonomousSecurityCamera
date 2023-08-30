import React from "react";
import {FaSearch} from "react-icons/fa";

export const SearchBar = ({ searchQuery, setSearchQuery}) => {
  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };
  return (
      <div className = 'searchBar'>
        <FaSearch id = "search-icon"></FaSearch>
        <input
          type="text"
          placeholder="Search videos..."
          value={searchQuery}
          onChange= {handleSearch}
        />
      </div>
  )
}

export default SearchBar;
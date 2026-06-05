resource "azurerm_resource_group" "demo" {
  name     = "student-rg"
  location = "East US"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "student-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = azurerm_resource_group.demo.location
  resource_group_name = azurerm_resource_group.demo.name
}

Changelog
=========

0.5.2 (2017-03-19)
------------------
* [infra] add missing actionlib dependencies

0.5.1 (2017-03-19)
------------------
* [tutorials] 6 - context switching
* [tutorials] re-insert missing images

0.5.0 (2017-02-21)
------------------
* [docs] new and shiny index added
* [tutorials] qt dashboard support
* [tutorials] 5 - tree scanning added
* [tutorials] 4 - tree introspection added
* [tutorials] 3 - blackboards added
* [tutorials] 2 - battery low branch added
* [tutorials] 1 - data gathering added
* [mock] a mock robot for tutorials and testing
* [behaviours] action client, battery behaviours added
* [infra] refactoring for kinetic

Indigo -> Kinetic Changelist
----------------------------

**Py Trees ROS API**

* **subscribers**

  * py_trees.subscribers.SubscriberHandler -> py_trees_ros.subscribers.Handler
  * py_trees.subscribers.CheckSubscriberVariable -> py_trees_ros.subscribers.CheckData
  * py_trees.subscribers.WaitForSubscriberData -> py_trees_ros.subscribers.WaitForData
* **conversions**

  * py_trees.converters.convert_type -> py_trees_ros.converters.behaviour_type_to_msg_constant
  * py_trees.converters.convert_status -> py_trees_ros.converters.status_enum_to_msg_constant
  * py_trees.converters.convert_blackbox -> py_trees_ros.converters.blackbox_enum_to_msg_constant
* **blackboard**

  * py_trees.ros.blackboard -> py_trees_ros.blackboard.Exchange
  * ~list_blackboard_variables -> ~get_blackboard_variables
  * ~spawn_blackboard_watcher -> ~open_blackboard_watcher
  * ~destroy_blackboard_watcher -> ~close_blackboard_watcher
* **visitors** : classes moved from py_trees.trees -> py_trees_ros.visitors

**Py Trees ROS Msgs API**

* **blackboard services**

  * py_trees.msgs.srv.BlackboardVariables -> py_trees_msgs.srv.GetBlackboardVariables
  * py_trees.msgs.srv.SpawnBlackboardWatcher -> py_trees_msgs.srv.OpenBlackboardWatcher
  * py_trees.msgs.srv.DestroyBlackboardWatcher -> py_trees_msgs.srv.CloseBlackboardWatcher

**Py Trees**

* **program** : py-trees-render added
* **imposter** : bugfix to permit visitors to the children of a composite original
* **visitors** : py_trees.trees -> py_trees.visitors
